# numpy and pandas for data manipulation
import pandas as pd
import numpy as np

# model used for feature importances
import lightgbm as lgb

# utility for early stopping with a validation set
from sklearn.model_selection import train_test_split

# visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# memory management
import gc

# utilities
from itertools import chain

class FeatureSelector():
    def __init__(self, data, labels=None):

        # Dataset and optional training labels
        self.data = data
        self.labels = labels

        if labels is None:
            print('No labels provided. Feature importance based methods are not available.')

        self.base_features = list(data.columns)
        self.one_hot_features = None

        # Dataframes recording information about features to remove
        self.record_missing = None
        self.record_single_unique = None
        self.record_collinear = None
        self.record_zero_importance = None
        self.record_low_importance = None

        self.missing_stats = None
        self.unique_stats = None
        self.corr_matrix = None
        self.feature_importances = None

        # Dictionary to hold removal operations
        self.ops = {}

        self.one_hot_correlated = False

    def identify_missing(self, missing_threshold):
        self.missing_threshold = missing_threshold

        # Calculate the fraction of missing in each column
        missing_series = self.data.isnull().sum() / self.data.shape[0]
        self.missing_stats = pd.DataFrame(missing_series).rename(columns={'index': 'feature', 0: 'missing_fraction'})

        # Sort with highest number of missing values on top
        self.missing_stats = self.missing_stats.sort_values('missing_fraction', ascending=False)

        # Find the columns with a missing percentage above the threshold
        record_missing = pd.DataFrame(missing_series[missing_series > missing_threshold]).reset_index().rename(columns=
                                                                                                               {
                                                                                                                   'index': 'feature',
                                                                                                                   0: 'missing_fraction'})

        to_drop = list(record_missing['feature'])

        self.record_missing = record_missing
        self.ops['missing'] = to_drop

        print('%d features with greater than %0.2f missing values.\n' % (
        len(self.ops['missing']), self.missing_threshold))

    def identify_single_unique(self):
        # Calculate the unique counts in each column
        unique_counts = self.data.nunique()
        self.unique_stats = pd.DataFrame(unique_counts).rename(columns={'index': 'feature', 0: 'nunique'})
        self.unique_stats = self.unique_stats.sort_values('nunique', ascending=True)

        # Find the columns with only one unique count
        record_single_unique = pd.DataFrame(unique_counts[unique_counts == 1]).reset_index().rename(
            columns={'index': 'feature',
                     0: 'nunique'})

        to_drop = list(record_single_unique['feature'])

        self.record_single_unique = record_single_unique
        self.ops['single_unique'] = to_drop

        print('%d features with a single unique value.\n' % len(self.ops['single_unique']))

    def identify_collinear(self, correlation_threshold, one_hot=False):
        self.correlation_threshold = correlation_threshold
        self.one_hot_correlated = one_hot

        # Calculate the correlations between every column
        if one_hot:

            # One hot encoding
            features = pd.get_dummies(self.data)
            self.one_hot_features = [column for column in features.columns if column not in self.base_features]

            # Add one hot encoded data to original data
            self.data_all = pd.concat([features[self.one_hot_features], self.data], axis=1)

            corr_matrix = pd.get_dummies(features).corr()

        else:
            corr_matrix = self.data.corr()

        self.corr_matrix = corr_matrix

        # Extract the upper triangle of the correlation matrix
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

        # Select the features with correlations above the threshold
        # Need to use the absolute value
        to_drop = [column for column in upper.columns if any(upper[column].abs() > correlation_threshold)]

        # Dataframe to hold correlated pairs
        record_collinear = pd.DataFrame(columns=['drop_feature', 'corr_feature', 'corr_value'])

        # Iterate through the columns to drop to record pairs of correlated features
        for column in to_drop:
            print(column)
            # Find the correlated features
            corr_features = list(upper.index[upper[column].abs() > correlation_threshold])

            # Find the correlated values
            corr_values = list(upper[column][upper[column].abs() > correlation_threshold])
            drop_features = [column for _ in range(len(corr_features))]

            # Record the information (need a temp df for now)
            temp_df = pd.DataFrame.from_dict({'drop_feature': drop_features,
                                              'corr_feature': corr_features,
                                              'corr_value': corr_values})

            # Add to dataframe
            record_collinear = record_collinear.append(temp_df, ignore_index=True)

        self.record_collinear = record_collinear
        self.ops['collinear'] = to_drop

        print('%d features with a correlation magnitude greater than %0.2f.\n' % (
        len(self.ops['collinear']), self.correlation_threshold))

    def identify_zero_importance(self, task, eval_metric=None,
                                 n_iterations=10, early_stopping=True):

        if early_stopping and eval_metric is None:
            raise ValueError("""eval metric must be provided with early stopping. Examples include "auc" for classification or
                             "l2" for regression.""")

        if self.labels is None:
            raise ValueError("No training labels provided.")

        # One hot encoding
        features = pd.get_dummies(self.data)
        self.one_hot_features = [column for column in features.columns if column not in self.base_features]

        # Add one hot encoded data to original data
        self.data_all = pd.concat([features[self.one_hot_features], self.data], axis=1)

        # Extract feature names
        feature_names = list(features.columns)

        # Convert to np array
        features = np.array(features)
        labels = np.array(self.labels).reshape((-1,))

        # Empty array for feature importances
        feature_importance_values = np.zeros(len(feature_names))

        print('Training Gradient Boosting Model\n')

        # Iterate through each fold
        for _ in range(n_iterations):

            if task == 'classification':
                model = lgb.LGBMClassifier(n_estimators=1000, learning_rate=0.05, verbose=-1)

            elif task == 'regression':
                model = lgb.LGBMRegressor(n_estimators=1000, learning_rate=0.05, verbose=-1)

            else:
                raise ValueError('Task must be either "classification" or "regression"')

            # If training using early stopping need a validation set
            if early_stopping:

                train_features, valid_features, train_labels, valid_labels = train_test_split(features, labels,
                                                                                              test_size=0.15,
                                                                                              stratify=labels)

                # Train the model with early stopping
                model.fit(train_features, train_labels, eval_metric=eval_metric,
                          eval_set=[(valid_features, valid_labels)],
                          early_stopping_rounds=100, verbose=-1)

                # Clean up memory
                gc.enable()
                del train_features, train_labels, valid_features, valid_labels
                gc.collect()

            else:
                model.fit(features, labels)

            # Record the feature importances
            feature_importance_values += model.feature_importances_ / n_iterations

        feature_importances = pd.DataFrame({'feature': feature_names, 'importance': feature_importance_values})

        # Sort features according to importance
        feature_importances = feature_importances.sort_values('importance', ascending=False).reset_index(drop=True)

        # Normalize the feature importances to add up to one
        feature_importances['normalized_importance'] = feature_importances['importance'] / feature_importances[
            'importance'].sum()
        feature_importances['cumulative_importance'] = np.cumsum(feature_importances['normalized_importance'])

        # Extract the features with zero importance
        record_zero_importance = feature_importances[feature_importances['importance'] == 0.0]

        to_drop = list(record_zero_importance['feature'])

        self.feature_importances = feature_importances
        self.record_zero_importance = record_zero_importance
        self.ops['zero_importance'] = to_drop

        print('\n%d features with zero importance after one-hot encoding.\n' % len(self.ops['zero_importance']))

    def identify_low_importance(self, cumulative_importance):
        self.cumulative_importance = cumulative_importance

        # The feature importances need to be calculated before running
        if self.feature_importances is None:
            raise NotImplementedError("""Feature importances have not yet been determined. 
                                         Call the `identify_zero_importance` method first.""")

        # Make sure most important features are on top
        self.feature_importances = self.feature_importances.sort_values('cumulative_importance')

        # Identify the features not needed to reach the cumulative_importance
        record_low_importance = self.feature_importances[
            self.feature_importances['cumulative_importance'] > cumulative_importance]

        to_drop = list(record_low_importance['feature'])

        self.record_low_importance = record_low_importance
        self.ops['low_importance'] = to_drop

        print('%d features required for cumulative importance of %0.2f after one hot encoding.' % (
        len(self.feature_importances) -
        len(self.record_low_importance), self.cumulative_importance))
        print('%d features do not contribute to cumulative importance of %0.2f.\n' % (len(self.ops['low_importance']),
                                                                                      self.cumulative_importance))

    def identify_all(self, selection_params):
        # Check for all required parameters
        for param in ['missing_threshold', 'correlation_threshold', 'eval_metric', 'task', 'cumulative_importance']:
            if param not in selection_params.keys():
                raise ValueError('%s is a required parameter for this method.' % param)

        # Implement each of the five methods
        self.identify_missing(selection_params['missing_threshold'])
        self.identify_single_unique()
        self.identify_collinear(selection_params['correlation_threshold'])
        self.identify_zero_importance(task=selection_params['task'], eval_metric=selection_params['eval_metric'])
        self.identify_low_importance(selection_params['cumulative_importance'])

        # Find the number of features identified to drop
        self.all_identified = set(list(chain(*list(self.ops.values()))))
        self.n_identified = len(self.all_identified)

        print('%d total features out of %d identified for removal after one-hot encoding.\n' % (self.n_identified,
                                                                                                self.data_all.shape[1]))

    def check_removal(self, keep_one_hot=True):
        self.all_identified = set(list(chain(*list(self.ops.values()))))
        print('Total of %d features identified for removal' % len(self.all_identified))

        if not keep_one_hot:
            if self.one_hot_features is None:
                print('Data has not been one-hot encoded')
            else:
                one_hot_to_remove = [x for x in self.one_hot_features if x not in self.all_identified]
                print('%d additional one-hot features can be removed' % len(one_hot_to_remove))

        return list(self.all_identified)

    def remove(self, methods, keep_one_hot=True):
        features_to_drop = []

        if methods == 'all':

            # Need to use one-hot encoded data as well
            data = self.data_all

            print('{} methods have been run\n'.format(list(self.ops.keys())))

            # Find the unique features to drop
            features_to_drop = set(list(chain(*list(self.ops.values()))))

        else:
            # Need to use one-hot encoded data as well
            if 'zero_importance' in methods or 'low_importance' in methods or self.one_hot_correlated:
                data = self.data_all

            else:
                data = self.data

            # Iterate through the specified methods
            for method in methods:

                # Check to make sure the method has been run
                if method not in self.ops.keys():
                    raise NotImplementedError('%s method has not been run' % method)

                # Append the features identified for removal
                else:
                    features_to_drop.append(self.ops[method])

            # Find the unique features to drop
            features_to_drop = set(list(chain(*features_to_drop)))

        features_to_drop = list(features_to_drop)

        if not keep_one_hot:

            if self.one_hot_features is None:
                print('Data has not been one-hot encoded')
            else:

                features_to_drop = list(set(features_to_drop) | set(self.one_hot_features))

        # Remove the features and return the data
        data = data.drop(columns=features_to_drop)
        self.removed_features = features_to_drop

        if not keep_one_hot:
            print('Removed %d features including one-hot features.' % len(features_to_drop))
        else:
            print('Removed %d features.' % len(features_to_drop))

        return data

    def plot_missing(self):
        if self.record_missing is None:
            raise NotImplementedError("Missing values have not been calculated. Run `identify_missing`")

        self.reset_plot()

        # Histogram of missing values
        plt.style.use('seaborn-white')
        plt.figure(figsize=(7, 5))
        plt.hist(self.missing_stats['missing_fraction'], bins=np.linspace(0, 1, 11), edgecolor='k', color='red',
                 linewidth=1.5)
        plt.xticks(np.linspace(0, 1, 11))
        plt.xlabel('Missing Fraction', size=14)
        plt.ylabel('Count of Features', size=14)
        plt.title("Fraction of Missing Values Histogram", size=16)
        plt.show()

    def plot_unique(self):
        if self.record_single_unique is None:
            raise NotImplementedError('Unique values have not been calculated. Run `identify_single_unique`')

        self.reset_plot()

        # Histogram of number of unique values
        self.unique_stats.plot.hist(edgecolor='k', figsize=(7, 5))
        plt.ylabel('Frequency', size=14)
        plt.xlabel('Unique Values', size=14)
        plt.title('Number of Unique Values Histogram', size=16)
        plt.show()

    def plot_collinear(self, plot_all=False):
        if self.record_collinear is None:
            raise NotImplementedError('Collinear features have not been idenfitied. Run `identify_collinear`.')

        if plot_all:
            corr_matrix_plot = self.corr_matrix
            title = 'All Correlations'

        else:
            # Identify the correlations that were above the threshold
            # columns (x-axis) are features to drop and rows (y_axis) are correlated pairs
            corr_matrix_plot = self.corr_matrix.loc[list(set(self.record_collinear['corr_feature'])),
                                                    list(set(self.record_collinear['drop_feature']))]

            title = "Correlations Above Threshold"

        f, ax = plt.subplots(figsize=(10, 8))

        # Diverging colormap
        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        # Draw the heatmap with a color bar
        sns.heatmap(corr_matrix_plot, cmap=cmap, center=0,
                    linewidths=.25, cbar_kws={"shrink": 0.6})

        # Set the ylabels
        ax.set_yticks([x + 0.5 for x in list(range(corr_matrix_plot.shape[0]))])
        ax.set_yticklabels(list(corr_matrix_plot.index), size=int(160 / corr_matrix_plot.shape[0]))

        # Set the xlabels
        ax.set_xticks([x + 0.5 for x in list(range(corr_matrix_plot.shape[1]))])
        ax.set_xticklabels(list(corr_matrix_plot.columns), size=int(160 / corr_matrix_plot.shape[1]))
        plt.title(title, size=14)
        plt.show()

    def plot_feature_importances(self, plot_n=15, threshold=None):
        if self.record_zero_importance is None:
            raise NotImplementedError('Feature importances have not been determined. Run `idenfity_zero_importance`')

        # Need to adjust number of features if greater than the features in the data
        if plot_n > self.feature_importances.shape[0]:
            plot_n = self.feature_importances.shape[0] - 1

        self.reset_plot()

        # Make a horizontal bar chart of feature importances
        plt.figure(figsize=(10, 6))
        ax = plt.subplot()

        # Need to reverse the index to plot most important on top
        # There might be a more efficient method to accomplish this
        ax.barh(list(reversed(list(self.feature_importances.index[:plot_n]))),
                self.feature_importances['normalized_importance'][:plot_n],
                align='center', edgecolor='k')

        # Set the yticks and labels
        ax.set_yticks(list(reversed(list(self.feature_importances.index[:plot_n]))))

        fi = []
        l = list(range(8, 60, 8))
        l.reverse()

        for str in self.feature_importances['feature'][:plot_n]:
            for i in range(60, 0, -8):
                if len(str) > i:
                    idx = str.find(' ', i)
                    if idx > 0:
                        str = str[:idx] + '\n' + str[idx + 1:]

            fi.append(str)

        ax.set_yticklabels(fi,
                           size=10,
                           verticalalignment='center')

        # Plot labeling
        plt.xlabel('Нормализованная значимость', size=16)
        plt.title('Значимость признаков', size=18)
        plt.show()

        # Cumulative importance plot
        plt.figure(figsize=(8, 4))
        plt.plot(list(range(1, len(self.feature_importances) + 1)), self.feature_importances['cumulative_importance'],
                 'r-')
        plt.xlabel('Число признаков', size=14)
        plt.ylabel('Кумулятивная важность', size=14)
        plt.title('Кумулятивная важность признаков', size=16)

        if threshold:
            # Index of minimum number of features needed for cumulative importance threshold
            # np.where returns the index so need to add 1 to have correct number
            importance_index = np.min(np.where(self.feature_importances['cumulative_importance'] > threshold))
            plt.vlines(x=importance_index + 1, ymin=0, ymax=1, linestyles='--', colors='blue')
            plt.show()

            print('%d features required for %0.2f of cumulative importance' % (importance_index + 1, threshold))

    def reset_plot(self):
        plt.rcParams = plt.rcParamsDefault
