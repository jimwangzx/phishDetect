import os
import pandas

headers = {
    'stats': [
        'коэффициент уникальности всех слов',

        #   URL FEATURES

        'наличие ip-адреса в url',
        'использование сервисов сокраения url',

        "наличие сертификата",
        "хороший netloc",

        'длина url',

        'кол-во @ в url',
        'кол-во ! в url',
        'кол-во + в url',
        'кол-во [ и ] в url',
        'кол-во ( и ) в url',
        'кол-во , в url',
        'кол-во $ в url',
        'кол-во ; в url',
        'кол-во пропусков в url',
        'кол-во & в url',
        'кол-во // в url',
        'кол-во / в url',
        'кол-во = в url',
        'кол-во % в url',
        'кол-во ? в url',
        'кол-во _ в url',
        'кол-во - в url',
        'кол-во . в url',
        'кол-во : в url',
        'кол-во * в url',
        'кол-во | в url',
        'кол-во ~ в url',
        'кол-во http токенов в url',

        'https',

        'соотношение цифр в url',
        'кол-во цифр в url',

        "кол-во фишинговых слов в url",
        "кол-во распознанных слов в url",

        'tld в пути url',
        'tld в поддомене url',
        'tld на плохой позиции url',
        'ненормальный поддомен url',

        'кол-во перенаправлений на сайт',
        'кол-во перенаправлений на другие домены',

        'случайный домен',

        'кол-во случайных слов в url',
        'кол-во случайных слов в хосте url',
        'кол-во случайных слов в пути url',

        'кол-во повторяющих последовательностей в url',
        'кол-во повторяющих последовательностей в хосте url',
        'кол-во повторяющих последовательностей в пути url',

        'наличие punycode',
        'домен в брендах',
        'юренд в пути url',
        'кол-во www в url',
        'кол-во com в url',

        'наличие порта в url',

        'кол-во слов в url',
        'средняя длина слова в url',
        'максимальная длина слова в url',
        'минимальная длина слова в url',

        'префикс суффикс в url',

        'кол-во поддоменов',

        'кол-во визульно схожих доменов',

        #   CONTENT FEATURE
        #       (static)

        'степень сжатия страницы',
        'кол-во полей ввода/вывода в основном контексте страницы',
        'соотношение кода в странице в основном контексте страницы',

        'кол-во всех ссылок в основном контексте страницы',
        'соотношение внутренних ссылок на сайты со всеми в основном контексте страницы',
        'соотношение внешних ссылок на сайты со всеми в основном контексте страницы',
        'соотношение пустых ссылок на сайты со всеми в основном контексте страницы',
        "соотношение внутренних CSS со всеми в основном контексте страницы",
        "соотношение внешних CSS со всеми в основном контексте страницы",
        "соотношение встроенных CSS со всеми в основном контексте страницы",
        "соотношение внутренних скриптов со всеми в основном контексте страницы",
        "соотношение внешних скриптов со всеми в основном контексте страницы",
        "соотношение встроенных скриптов со всеми в основном контексте страницы",
        "соотношение внешних изображений со всеми в основном контексте страницы",
        "соотношение внутренних изображений со всеми в основном контексте страницы",
        "общее кол-во перенаправлений по внутренним ссылкам в основном контексте страницы",
        "общее кол-во перенаправлений по внешним ссылкам в основном контексте страницы",
        "общее кол-во ошибок по внутренним ссылкам в основном контексте страницы",
        "общее кол-во ошибок по внешним ссылкам в основном контексте страницы",
        "форма входа в основном контексте страницы",
        "соотношение внешних Favicon со всеми в основном контексте страницы",
        "соотношение внутренних Favicon со всеми в основном контексте страницы",
        "наличие отправки на почту в основном контексте страницы",
        "соотношение внешних медиа со всеми в основном контексте страницы",
        "соотношение внешних медиа со всеми в основном контексте страницы",
        "пустой титульник в основном контексте страницы",
        "соотношение небезопасных якорей со всеми в основном контексте страницы",
        "соотношение безопасных якорей со всеми в основном контексте страницы",
        "соотношение внутренних ссылок на ресурсы со всеми в основном контексте страницы",
        "соотношение внешних ссылок на ресурсы со всеми в основном контексте страницы",
        "наличие невидимых в основном контексте страницы",
        "наличие onmouseover в основном контексте страницы",
        "наличие всплывающих окон в основном контексте страницы",
        "наличие событий правой мыши в основном контексте страницы",
        "наличие домена в тексте в основном контексте страницы",
        "наличие домена в титульнике в основном контексте страницы",
        "домен с авторскими правами в основном контексте страницы",
        "кол-во фишинговых слов в тексте в основном контексте страницы",
        "кол-во слов в тексте в основном контексте страницы",
        "соотношение текста со всех изображений с основным текстом в основном контексте страницы",
        "соотношение текста внутренних изображений с основным текстом в основном контексте страницы",
        "соотношение текста внешних изображений с основным текстом в основном контексте страницы",
        "соотношение текста внешних изображений с текстом внутренних изображений в основном контексте страницы",

        #       (dynamic)

        "соотношение основного текста с динамически добавляемым текстом страницы",

        #       (dynamic internals)

        "соотношение основного текста с внутреннее добавляемым текстом страницы",
        "соотношение кода в внутренне добавляемом контексте страницы",
        "кол-во полей ввода/вывода в внутренне добавляемом контексте страницы",

        'кол-во всех ссылок во внутренне добавляемом контексте страницы',
        'соотношение внутренних ссылок на сайты со всеми во внутренне добавляемом контексте страницы',
        'соотношение внешних ссылок на сайты со всеми во внутренне добавляемом контексте страницы',
        'соотношение пустых ссылок на сайты со всеми во внутренне добавляемом контексте страницы',
        "соотношение внутренних CSS со всеми во внутренне добавляемом контексте страницы",
        "соотношение внешних CSS со всеми во внутренне добавляемом контексте страницы",
        "соотношение встроенных CSS со всеми во внутренне добавляемом контексте страницы",
        "соотношение внутренних скриптов со всеми во внутренне добавляемом контексте страницы",
        "соотношение внешних скриптов со всеми во внутренне добавляемом контексте страницы",
        "соотношение встроенных скриптов со всеми во внутренне добавляемом контексте страницы",
        "соотношение внешних изображений со всеми во внутренне добавляемом контексте страницы",
        "соотношение внутренних изображений со всеми во внутренне добавляемом контексте страницы",
        "общее кол-во перенаправлений по внутренним ссылкам во внутренне добавляемом контексте страницы",
        "общее кол-во перенаправлений по внешним ссылкам во внутренне добавляемом контексте страницы",
        "общее кол-во ошибок по внутренним ссылкам во внутренне добавляемом контексте страницы",
        "общее кол-во ошибок по внешним ссылкам во внутренне добавляемом контексте страницы",
        "форма входа во внутренне добавляемом контексте страницы",
        "соотношение внешних Favicon со всеми во внутренне добавляемом контексте страницы",
        "соотношение внутренних Favicon со всеми во внутренне добавляемом контексте страницы",
        "наличие отправки на почту во внутренне добавляемом контексте страницы",
        "соотношение внешних медиа со всеми во внутренне добавляемом контексте страницы",
        "соотношение внешних медиа со всеми во внутренне добавляемом контексте страницы",
        "пустой титульник во внутренне добавляемом контексте страницы",
        "соотношение небезопасных якорей со всеми во внутренне добавляемом контексте страницы",
        "соотношение безопасных якорей со всеми во внутренне добавляемом контексте страницы",
        "соотношение внутренних ссылок на ресурсы со всеми во внутренне добавляемом контексте страницы",
        "соотношение внешних ссылок на ресурсы со всеми во внутренне добавляемом контексте страницы",
        "наличие невидимых во внутренне добавляемом контексте страницы",
        "наличие onmouseover во внутренне добавляемом контексте страницы",
        "наличие всплывающих окон во внутренне добавляемом контексте страницы",
        "наличие событий правой мыши во внутренне добавляемом контексте страницы",
        "наличие домена в тексте во внутренне добавляемом контексте страницы",
        "наличие домена в титульнике во внутренне добавляемом контексте страницы",
        "домен с авторскими правами во внутренне добавляемом контексте страницы",

        "кол-во операций ввода/вывода во внутренне добавляемом коде страницы",
        "кол-во фишинговых слов во внутренне добавляемом контексте страницы",
        "кол-во слов во внутренне добавляемом контексте страницы",

        #       (dynamic externals)

        "соотношение основного текста с внешне добавляемым текстом страницы",
        "соотношение кода в внешне добавляемом контексте страницы",
        "кол-во полей ввода/вывода в внешне добавляемом контексте страницы",

        'кол-во всех ссылок во внешне добавляемом контексте страницы',
        'соотношение внутренних ссылок на сайты со всеми во внешне добавляемом контексте страницы',
        'соотношение внешних ссылок на сайты со всеми во внешне добавляемом контексте страницы',
        'соотношение пустых ссылок на сайты со всеми во внешне добавляемом контексте страницы',
        "соотношение внутренних CSS со всеми во внешне добавляемом контексте страницы",
        "соотношение внешних CSS со всеми во внешне добавляемом контексте страницы",
        "соотношение встроенных CSS со всеми во внешне добавляемом контексте страницы",
        "соотношение внутренних скриптов со всеми во внешне добавляемом контексте страницы",
        "соотношение внешних скриптов со всеми во внешне добавляемом контексте страницы",
        "соотношение встроенных скриптов со всеми во внешне добавляемом контексте страницы",
        "соотношение внешних изображений со всеми во внешне добавляемом контексте страницы",
        "соотношение внутренних изображений со всеми во внешне добавляемом контексте страницы",
        "общее кол-во перенаправлений по внутренним ссылкам во внешне добавляемом контексте страницы",
        "общее кол-во перенаправлений по внешним ссылкам во внешне добавляемом контексте страницы",
        "общее кол-во ошибок по внутренним ссылкам во внешне добавляемом контексте страницы",
        "общее кол-во ошибок по внешним ссылкам во внешне добавляемом контексте страницы",
        "форма входа во внешне добавляемом контексте страницы",
        "соотношение внешних Favicon со всеми во внешне добавляемом контексте страницы",
        "соотношение внутренних Favicon со всеми во внешне добавляемом контексте страницы",
        "наличие отправки на почту во внешне добавляемом контексте страницы",
        "соотношение внешних медиа со всеми во внешне добавляемом контексте страницы",
        "соотношение внешних медиа со всеми во внешне добавляемом контексте страницы",
        "пустой титульник во внешне добавляемом контексте страницы",
        "соотношение небезопасных якорей со всеми во внешне добавляемом контексте страницы",
        "соотношение безопасных якорей со всеми во внешне добавляемом контексте страницы",
        "соотношение внутренних ссылок на ресурсы со всеми во внешне добавляемом контексте страницы",
        "соотношение внешних ссылок на ресурсы со всеми во внешне добавляемом контексте страницы",
        "наличие невидимых во внешне добавляемом контексте страницы",
        "наличие onmouseover во внешне добавляемом контексте страницы",
        "наличие всплывающих окон во внешне добавляемом контексте страницы",
        "наличие событий правой мыши во внешне добавляемом контексте страницы",
        "наличие домена в тексте во внешне добавляемом контексте страницы",
        "наличие домена в титульнике во внешне добавляемом контексте страницы",
        "домен с авторскими правами во внешне добавляемом контексте страницы",

        "кол-во операций ввода/вывода во внешне добавляемом коде страницы",
        "кол-во фишинговых слов во внешне добавляемом контексте страницы",
        "кол-во слов во внешне добавляемом контексте страницы",

        #   EXTERNAL FEATURES

        'срок регистрации домена',
        "домен зарегестрирован",
        "рейтинг по Alexa",
        "рейтинг по openpagerank",
        "соотношение оставшегося времени действия сертификата",
        "срок действия сертификата",
        "кол-во альтернативных имен в сертификате"
    ],
    # 'stats': [
    #     'word_ratio',
    #
    #                 #   URL FEATURES
    #
    #                 'uf.having_ip_address(url)',
    #                 'uf.shortening_service(url)',
    #
    #                 "cert!=None",
    #                 "good_netloc",
    #
    #                 'uf.url_length(r_url)',
    #
    #                 'uf.count_at(r_url)',
    #                 'uf.count_exclamation(r_url)',
    #                 'uf.count_plust(r_url)',
    #                 'uf.count_sBrackets(r_url)',
    #                 'uf.count_rBrackets(r_url)',
    #                 'uf.count_comma(r_url)',
    #                 'uf.count_dollar(r_url)',
    #                 'uf.count_semicolumn(r_url)',
    #                 'uf.count_space(r_url)',
    #                 'uf.count_and(r_url)',
    #                 'uf.count_double_slash(r_url)',
    #                 'uf.count_slash(r_url)',
    #                 'uf.count_equal(r_url)',
    #                 'uf.count_percentage(r_url)',
    #                 'uf.count_question(r_url)',
    #                 'uf.count_underscore(r_url)',
    #                 'uf.count_hyphens(r_url)',
    #                 'uf.count_dots(r_url)',
    #                 'uf.count_colon(r_url)',
    #                 'uf.count_star(r_url)',
    #                 'uf.count_or(r_url)',
    #                 'uf.count_tilde(r_url)',
    #                 'uf.count_http_token(r_url)',
    #
    #                 'uf.https_token(scheme)',
    #
    #                 'uf.ratio_digits(r_url)',
    #                 'uf.count_digits(r_url)',
    #
    #                 "cf.count_phish_hints(url_words, phish_hints)",
    #                 "(len(url_words), 0)",
    #
    #                 'uf.tld_in_path(tld,path)',
    #                 'uf.tld_in_subdomain(tld,subdomain)',
    #                 'uf.tld_in_bad_position(tld,subdomain,path)',
    #                 'uf.abnormal_subdomain(r_url)',
    #
    #                 'uf.count_redirection(request)',
    #                 'uf.count_external_redirection(request,domain)',
    #
    #                 'uf.random_domain(second_level_domain)',
    #
    #                 'uf.random_words(words_raw)',
    #                 'uf.random_words(words_raw_host)',
    #                 'uf.random_words(words_raw_path)',
    #
    #                 'uf.char_repeat(words_raw)',
    #                 'uf.char_repeat(words_raw_host)',
    #                 'uf.char_repeat(words_raw_path)',
    #
    #                 'uf.punycode(r_url)',
    #                 'uf.domain_in_brand(second_level_domain)',
    #                 'uf.brand_in_path(second_level_domain, words_raw_path)',
    #                 'uf.check_www(words_raw)',
    #                 'uf.check_com(words_raw)',
    #
    #                 'uf.port(r_url)',
    #
    #                 'uf.length_word_raw(words_raw)',
    #                 'uf.average_word_length(words_raw)',
    #                 'uf.longest_word_length(words_raw)',
    #                 'uf.shortest_word_length(words_raw)',
    #
    #                 'uf.prefix_suffix(r_url)',
    #
    #                 'uf.count_subdomain(r_url)',
    #
    #                 'uf.count_visual_similarity_domains(second_level_domain)',
    #
    #                 #   CONTENT FEATURE
    #                 #       (static)
    #
    #                 'cf.compression_ratio(request)',
    #                 'cf.count_textareas(content)',
    #                 'cf.ratio_js_on_html(Text)',
    #
    #                 'len(iUrl_s)+len(eUrl_s)',
    #                 'cf.urls_ratio(iUrl_s,iUrl_s+eUrl_s+nUrl_s)',
    #                 'cf.urls_ratio(eUrl_s,iUrl_s+eUrl_s+nUrl_s)',
    #                 'cf.urls_ratio(nUrl_s,iUrl_s+eUrl_s+nUrl_s)',
    #                 "cf.ratio_List(CSS,'internals')",
    #                 "cf.ratio_List(CSS,'externals')",
    #                 "cf.ratio_List(CSS,'embedded')",
    #                 "cf.ratio_List(SCRIPT,'internals')",
    #                 "cf.ratio_List(SCRIPT,'externals')",
    #                 "cf.ratio_List(SCRIPT,'embedded')",
    #                 "cf.ratio_List(Img,'externals')",
    #                 "cf.ratio_List(Img,'internals')",
    #                 "cf.count_reqs_redirections(reqs_iData_s)",
    #                 "cf.count_reqs_redirections(reqs_eData_s)",
    #                 "cf.count_reqs_error(reqs_iData_s)",
    #                 "cf.count_reqs_error(reqs_eData_s)",
    #                 "cf.login_form(Form)",
    #                 "cf.ratio_List(Favicon,'externals')",
    #                 "cf.ratio_List(Favicon,'internals')",
    #                 "cf.submitting_to_email(Form)",
    #                 "cf.ratio_List(Media,'internals')",
    #                 "cf.ratio_List(Media,'externals')",
    #                 "cf.empty_title(Title)",
    #                 "cf.ratio_anchor(Anchor,'unsafe')",
    #                 "cf.ratio_anchor(Anchor,'safe')",
    #                 "cf.ratio_List(Link,'internals')",
    #                 "cf.ratio_List(Link,'externals')",
    #                 "cf.iframe(IFrame)",
    #                 "cf.onmouseover(content)",
    #                 "cf.popup_window(content)",
    #                 "cf.right_clic(content)",
    #                 "cf.domain_in_text(second_level_domain,Text)",
    #                 "cf.domain_in_text(second_level_domain,Title)",
    #                 "cf.domain_with_copyright(domain,content)",
    #                 "cf.count_phish_hints(Text, phish_hints)",
    #                 "(len(sContent_words), 0)",
    #                 "cf.ratio_Txt(iImgTxt_words+eImgTxt_words,sContent_words)",
    #                 "cf.ratio_Txt(iImgTxt_words,sContent_words)",
    #                 "cf.ratio_Txt(eImgTxt_words,sContent_words)",
    #                 "cf.ratio_Txt(eImgTxt_words,iImgTxt_words)",
    #
    #                 #       (dynamic)
    #
    #                 "cf.ratio_dynamic_html(Text,"".join([Text_di,Text_de]))",
    #
    #                 #       (dynamic internals)
    #
    #                 "cf.ratio_dynamic_html(Text,Text_di)",
    #                 "cf.ratio_js_on_html(Text_di)",
    #                 "cf.count_textareas(content_di)",
    #
    #                 "len(iUrl_di)+len(eUrl_di)",
    #                 "cf.urls_ratio(iUrl_di,iUrl_di+eUrl_di+nUrl_di)",
    #                 "cf.urls_ratio(eUrl_di,iUrl_di+eUrl_di+nUrl_di)",
    #                 "cf.urls_ratio(nUrl_di,iUrl_di+eUrl_di+nUrl_di)",
    #                 "cf.ratio_List(CSS_di,'internals')",
    #                 "cf.ratio_List(CSS_di,'externals')",
    #                 "cf.ratio_List(CSS_di,'embedded')",
    #                 "cf.ratio_List(SCRIPT_di,'internals')",
    #                 "cf.ratio_List(SCRIPT_di,'externals')",
    #                 "cf.ratio_List(SCRIPT_di,'embedded')",
    #                 "cf.ratio_List(Img_di,'externals')",
    #                 "cf.ratio_List(Img_di,'internals')",
    #                 "cf.count_reqs_redirections(reqs_iData_di)",
    #                 "cf.count_reqs_redirections(reqs_eData_di)",
    #                 "cf.count_reqs_error(reqs_iData_di)",
    #                 "cf.count_reqs_error(reqs_eData_di)",
    #                 "cf.login_form(Form_di)",
    #                 "cf.ratio_List(Favicon_di,'externals')",
    #                 "cf.ratio_List(Favicon_di,'internals')",
    #                 "cf.submitting_to_email(Form_di)",
    #                 "cf.ratio_List(Media_di,'internals')",
    #                 "cf.ratio_List(Media_di,'externals')",
    #                 "cf.empty_title(Title_di)",
    #                 "cf.ratio_anchor(Anchor_di,'unsafe')",
    #                 "cf.ratio_anchor(Anchor_di,'safe')",
    #                 "cf.ratio_List(Link_di,'internals')",
    #                 "cf.ratio_List(Link_di,'externals')",
    #                 "cf.iframe(IFrame_di)",
    #                 "cf.onmouseover(content_di)",
    #                 "cf.popup_window(content_di)",
    #                 "cf.right_clic(content_di)",
    #                 "cf.domain_in_text(second_level_domain,Text_di)",
    #                 "cf.domain_in_text(second_level_domain,Title_di)",
    #                 "cf.domain_with_copyright(domain,content_di)",
    #
    #                 "cf.count_io_commands(internals_script_doc)",
    #                 "cf.count_phish_hints(Text_di,phish_hints)",
    #                 "(len(diContent_words), 0)",
    #
    #                 #       (dynamic externals)
    #
    #                 "cf.ratio_dynamic_html(Text,Text_de)",
    #                 "cf.ratio_js_on_html(Text_de)",
    #                 "cf.count_textareas(content_de)",
    #
    #                 "len(iUrl_de)+len(eUrl_de)",
    #                 "cf.urls_ratio(iUrl_de,iUrl_de+eUrl_de+nUrl_de)",
    #                 "cf.urls_ratio(eUrl_de,iUrl_de+eUrl_de+nUrl_de)",
    #                 "cf.urls_ratio(nUrl_de,iUrl_de+eUrl_de+nUrl_de)",
    #                 "cf.ratio_List(CSS_de,'internals')",
    #                 "cf.ratio_List(CSS_de,'externals')",
    #                 "cf.ratio_List(CSS_de,'embedded')",
    #                 "cf.ratio_List(SCRIPT_de,'internals')",
    #                 "cf.ratio_List(SCRIPT_de,'externals')",
    #                 "cf.ratio_List(SCRIPT_de,'embedded')",
    #                 "cf.ratio_List(Img_de,'externals')",
    #                 "cf.ratio_List(Img_de,'internals')",
    #                 "cf.count_reqs_redirections(reqs_iData_de)",
    #                 "cf.count_reqs_redirections(reqs_eData_de)",
    #                 "cf.count_reqs_error(reqs_iData_de)",
    #                 "cf.count_reqs_error(reqs_eData_de)",
    #                 "cf.login_form(Form_de)",
    #                 "cf.ratio_List(Favicon_de,'externals')",
    #                 "cf.ratio_List(Favicon_de,'internals')",
    #                 "cf.submitting_to_email(Form_de)",
    #                 "cf.ratio_List(Media_de,'internals')",
    #                 "cf.ratio_List(Media_de,'externals')",
    #                 "cf.empty_title(Title_de)",
    #                 "cf.ratio_anchor(Anchor_de,'unsafe')",
    #                 "cf.ratio_anchor(Anchor_de,'safe')",
    #                 "cf.ratio_List(Link_de,'internals')",
    #                 "cf.ratio_List(Link_de,'externals')",
    #                 "cf.iframe(IFrame_de)",
    #                 "cf.onmouseover(content_de)",
    #                 'cf.popup_window(content_de)',
    #                 "cf.right_clic(content_de)",
    #                 "cf.domain_in_text(second_level_domain,Text_de)",
    #                 "cf.domain_in_text(second_level_domain,Title_de)",
    #                 "cf.domain_with_copyright(domain,content_de)",
    #
    #                 "cf.count_io_commands(externals_script_doc)",
    #                 "cf.count_phish_hints(Text_de,phish_hints)",
    #                 "(len(deContent_words), 0)",
    #
    #                 #   EXTERNAL FEATURES
    #
    #                 'ef.domain_registration_length(domain)',
    #                 "ef.whois_registered_domain(domain)",
    #                 "ef.web_traffic(r_url)",
    #                 "ef.page_rank(domain)",
    #                 "ef.remainder_valid_cert(hostinfo.cert)",
    #                 "ef.valid_cert_period(hostinfo.cert)",
    #                 "ef.count_alt_names(hostinfo.cert)"
    # ],
    'metadata': [
        'url',
        'lang',
        'status'
    ],
    'substats': [
        'extraction-contextData-time',
        'image-recognition-time'
    ]
}

from hyperopt import hp, fmin, tpe, STATUS_OK, Trials
from matplotlib import pyplot as plt
import numpy as np
import json
import pickle
from shutil import move
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, recall_score, precision_score
from math import ceil

frame = pandas.read_csv('data/datasets/OUTPUT/dataset.csv')
cols = [col for col in headers['stats'] if col in list(frame)]
X = frame[cols].to_numpy()
Y = frame['status'].to_numpy()


def plot_lr(lr, n_epochs, decay):
    from math import exp

    path = [lr]

    for epoch in range(n_epochs):
        lr = lr * exp(-epoch / decay)
        path.append(lr)

    plt.plot(path)
    plt.title("изменение скорости обучения")
    plt.xlabel='эпоха'
    plt.ylabel='скорость обучения'
    plt.show()
    plt.clf()
    plt.close()


def plot_hyperop_score(dir):
    with open("data/trials/{}/results.pkl".format(dir), 'rb') as f:
        data = pickle.load(f)

    path = []
    max_v = 0.9
    for idx, raw in enumerate(data.results):
        if -raw['loss'] > max_v:
            max_v = -raw['loss']
        path.append(max_v)

    plt.plot(path)
    plt.title("подбор гиперпараметров")
    plt.xlabel = 'итерация'
    plt.ylabel = 'точность'
    plt.ylim(path[0]-0.01, path[-1]+0.01)
    plt.show()
    plt.clf()
    plt.close()


def draw(history, metrics, dir):
    h = ceil(len(metrics) / 2)
    fig, axs = plt.subplots(h, 2, figsize=(2 * 5, h * 5), dpi=400)

    for i in range(len(metrics)):
        axs[i % 3, i // 3].plot(history[metrics[i]])
        axs[i % 3, i // 3].plot(history['val_{}'.format(metrics[i])])
        axs[i % 3, i // 3].set(xlabel='epoch', ylabel=metrics[i])
        axs[i % 3, i // 3].set_title(metrics[i])
        axs[i % 3, i // 3].legend(['train', 'test'], loc='best')

    fig.savefig('data/trials/{}/stats.png'.format(dir))
    fig.clf()
    plt.close()


def get_rating():
    lst = os.listdir(os.getcwd() + '/data/trials')
    metrics = []
    for dir in lst:
        try:
            with open('data/trials/{}/metrics.json'.format(dir), 'r') as f:
                metrics.append({
                    'dir': dir,
                    'm': json.load(f)
                })
        except:
            pass
    acc = [m['m']['accuracy'] for m in metrics]
    pre = [m['m']['Precision'] for m in metrics]
    rec = [m['m']['Recall'] for m in metrics]
    auc = [m['m']['AUC'] for m in metrics]
    f_score = [m['m']['f_score'] for m in metrics]
    names = [m['dir'] for m in metrics]

    df = pandas.DataFrame([acc, pre, rec, auc, f_score]).T
    df.columns = ['accuracy', 'precision', 'recall', 'auc', 'f_score']
    df.index = names
    df.to_csv('data/trials/ratings.csv', index_label='algs')


def neural_networks_archSearch():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices --tf_xla_auto_jit=2 --tf_xla_cpu_global_jit'

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    import tensorflow as tf
    from tensorflow.keras import layers, models, optimizers, losses

    import telepot


    metrics = [
        'accuracy',
        'Precision',
        'Recall',
        'AUC'
    ]


    tf.compat.v1.enable_eager_execution()

    try:
        with open("data/trials/neural_networks_archSearch/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    def layer(N, M=-1):
        if M == -1:
            M = N
        if N == 0:
            return None
        return hp.choice('layer_{}'.format(M - N), [
            None,
            {
                'activation': hp.choice('activation_{}'.format(M - N), [
                    'selu',
                    'relu',
                    'softmax',
                    'sigmoid',
                    'softplus',
                    'softsign',
                    'tanh',
                    'elu',
                    'exponential'
                ]),
                'nodes_count': hp.randint('nodes_count_{}'.format(M - N), 500)+2,
                'dropout': hp.choice('dropout_{}'.format(M - N), [
                    {'dropout_rate': hp.uniform('dropout_rate_{}'.format(M - N), 0, 0.5)},
                    None
                ]),
                'BatchNormalization': hp.choice('BatchNormalization_{}'.format(M - N), [False, True]),
                'next': layer(N - 1, M)
            }
        ])

    space = {
        'decay_steps':
            hp.randint('decay_steps', 10000)*100,
        'layers': layer(5),
        'optimizer':
            hp.choice('optimizer', [
                {
                    'type': 'Adadelta',
                    'learning_rate': hp.uniform('Adadelta_lr', 0.001, 1),
                },
                {
                    'type': 'Adagrad',
                    'learning_rate': hp.uniform('Adagrad_lr', 0.001, 1),
                },
                {
                    'type': 'Adamax',
                    'learning_rate': hp.uniform('Adamax_lr', 0.001, 1),
                },
                {
                    'type': 'Adam',
                    'learning_rate': hp.uniform('Adam_lr', 0.001, 1),
                    'amsgrad': hp.choice('Adam_amsgrad', [False, True])
                },
                # {
                #     'type': 'Ftrl',
                #     'learning_rate': hp.uniform('Ftrl_lr', 0.001, 1),
                # },
                {
                    'type': 'Nadam',
                    'learning_rate': hp.uniform('Nadam_lr', 0.001, 1),
                },
                {
                    'type': 'RMSprop',
                    'learning_rate': hp.uniform('RMSprop_lr', 0.001, 1),
                    'centered': hp.choice('RMSprop_centered', [False, True]),
                    'momentum': hp.uniform('RMSprop_momentum', 0.001, 1),
                },
                {
                    'type': 'SGD',
                    'learning_rate': hp.uniform('SGD_lr', 0.001, 1),
                    'nesterov': hp.choice('SGD_nesterov', [False, True]),
                    'momentum': hp.uniform('SGD_momentum', 0.001, 1),
                }
            ]),
        'batch_size': 64,
        'init': hp.choice('init', [
            'glorot_normal',
            'truncated_normal',
            'glorot_uniform'
        ]),
        'trainable_BatchNormalization': hp.choice('trainable_BatchNormalization', [False, True]),
        'trainable_dropouts': hp.choice('trainable_dropouts', [False, True]),
        'shuffle': True
    }

    import tensorflow.keras.backend as K

    def f_score(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        recall = true_positives / (possible_positives + K.epsilon())
        f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
        return f1_val

    def objective(space):
        model = models.Sequential()

        layer = space['layers']

        while layer:
            model.add(layers.Dense(
                layer['nodes_count'],
                kernel_initializer=space['init'],
                activation=layer['activation'])
            )
            if layer['dropout']:
                model.add(layers.Dropout(layer['dropout']['dropout_rate'], trainable=space['trainable_dropouts']))
            if layer['BatchNormalization']:
                model.add(layers.BatchNormalization(trainable=space['trainable_BatchNormalization']))

            layer = layer['next']

        model.add(layers.Dense(1, kernel_initializer=space['init'], activation='sigmoid'))

        def scheduler(epoch, lr):
            return lr * tf.math.exp(-epoch / space['decay_steps'])

        def tf_callbacks():
            return [
                tf.keras.callbacks.ModelCheckpoint(
                    'data/models/neural_networks_archSearch/tmp.h5',
                    monitor='val_accuracy',
                    mode='max',
                    verbose=0,
                    save_best_only=True
                ),
                tf.keras.callbacks.EarlyStopping(
                    monitor='val_accuracy',
                    patience=25,
                    min_delta=0.00001,
                    mode='max',
                    verbose=0),
                tf.keras.callbacks.LearningRateScheduler(scheduler)
            ]

        if space['optimizer']['type'] == 'Adadelta':
            optimizer = optimizers.Adadelta()
        elif space['optimizer']['type'] == 'Adagrad':
            optimizer = optimizers.Adagrad()
        elif space['optimizer']['type'] == 'Adam':
            optimizer = optimizers.Adam()
        elif space['optimizer']['type'] == 'Adamax':
            optimizer = optimizers.Adamax()
        elif space['optimizer']['type'] == 'Ftrl':
            optimizer = optimizers.Ftrl()
        elif space['optimizer']['type'] == 'Nadam':
            optimizer = optimizers.Nadam()
        elif space['optimizer']['type'] == 'RMSprop':
            optimizer = optimizers.RMSprop()
        elif space['optimizer']['type'] == 'SGD':
            optimizer = optimizers.SGD()

        optimizer.learning_rate = space['optimizer']['learning_rate']
        if 'amsgrad' in space['optimizer']:
            optimizer.amsgrad = space['optimizer']['amsgrad']
        if 'centered' in space['optimizer']:
            optimizer.centered = space['optimizer']['centered']
        if 'momentrum' in space['optimizer']:
            optimizer.momentum = space['optimizer']['momentum']
        if 'nesterov' in space['optimizer']:
            optimizer.nesterov = space['optimizer']['nesterov']

        try:
            model.compile(
                optimizer=optimizer,
                loss=losses.BinaryCrossentropy(from_logits=True),
                metrics=metrics + [f_score]
            )

            history = model.fit(
                x_train, y_train,
                validation_data=(x_test, y_test),
                # validation_split=0.1,
                epochs=500,
                callbacks=tf_callbacks(),
                verbose=0,
                batch_size=space['batch_size'],
                shuffle=space['shuffle']
            )

            loss, acc, precision, recall, auc, fScore = model.evaluate(x_test, y_test, verbose=0)

            try:
                with open("data/trials/neural_networks_archSearch/metric.txt") as f:
                    max_fScore = float(f.read().strip())  # read best metric,
            except FileNotFoundError:
                max_fScore = -1

            m = {
                "loss": loss,
                "accuracy": acc,
                "Precision": precision,
                "Recall": recall,
                "AUC": auc,
                "f_score": fScore
            }

            if fScore > max_fScore:
                model.save("data/models/neural_networks_archSearch/nn1.h5")
                move('data/models/neural_networks_archSearch/tmp.h5', "data/models/neural_networks_archSearch/nn2.h5")
                with open("data/trials/neural_networks_archSearch/space.json", "w") as f:
                    f.write(str(space))
                with open("data/trials/neural_networks_archSearch/metric.txt", "w") as f:
                    f.write(str(fScore))
                with open("data/trials/neural_networks_archSearch/metrics.json", "w") as f:
                    json.dump(m, f)
                with open("data/trials/neural_networks_archSearch/history.pkl", 'wb') as f:
                    pickle.dump(history.history, f)

            try:
                telegram_info = pandas.read_csv('telegram_client.csv')
                bot = telepot.Bot(telegram_info['BOT_token'][0])
                bot.sendMessage(int(telegram_info['CHAT_ID'][0]), str(space))
                bot.sendMessage(int(telegram_info['CHAT_ID'][0]), str(m))
                draw(history.history, list(map(lambda x: x.lower(), metrics)) + ['loss', 'f_score'], 'neural_networks_archSearch')
                bot.sendPhoto(int(telegram_info['CHAT_ID'][0]), photo=open(
                    'data/trials/neural_networks_archSearch/stats.png', 'rb'))
            except:
                pass

            return {
                'loss': -fScore,
                'status': STATUS_OK,
                'history': history.history,
                'space': space,
                'metrics': m
            }
        except:
            return {
                'loss': 1,
                'status': STATUS_OK,
                'history': None,
                'space': space,
                'metrics': None
            }

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=1500,
                  # + len(trials),
        trials=trials,
        timeout=60 * 60 * 10
    )

    def typer(o):
        if isinstance(o, np.int32):
            return int(o)
        return o

    with open("data/trials/neural_networks_archSearch/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/neural_networks_archSearch/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def find_best_NN(throughput=0.01, gap=0.1):
    with open("data/trials/neural_networks_archSearch/results.pkl", 'rb') as f:
        data = pickle.load(f)

    metrics = []

    columns = [
        'id',
        'loss',
        'accuracy',
        'precision',
        'recall',
        'auc',
        'f_score'
    ]

    for idx, raw in enumerate(data.results):
        history = raw['history']

        if history:
            if (history['val_loss'][-1] - history['loss'][-1]) <= throughput \
                    and (history['val_accuracy'][-1] - history['accuracy'][-1]) >= -throughput \
                    and (history['val_f_score'][-1] - history['f_score'][-1]) >= -throughput\
                    and abs(history['val_loss'][-1] - history['loss'][-1]) <= gap\
                    and abs(history['val_accuracy'][-1] - history['accuracy'][-1]) <= gap\
                    and abs(history['val_f_score'][-1] - history['f_score'][-1]) <= gap:

                metrics.append([idx] + list(raw['metrics'].values()))

    id = pandas.DataFrame(metrics, columns=columns).sort_values(
        'f_score', ascending=False
    ).head(1)['id']

    # for i in df['id']:
    #     history = data.results[i]['history']
    #
    #     l = len(history['loss'])//4
    #
    #     stats.append([
    #         i,
    #         (np.array(history['val_loss'][-l:]) - np.array(history['loss'][-l:])).std(),
    #         (np.array(history['val_accuracy'][-l:]) - np.array(history['accuracy'][-l:])).std(),
    #         (np.array(history['val_precision'][-l:]) - np.array(history['precision'][-l:])).std(),
    #         (np.array(history['val_recall'][-l:]) - np.array(history['recall'][-l:])).std(),
    #         (np.array(history['val_auc'][-l:]) - np.array(history['auc'][-l:])).std(),
    #         (np.array(history['val_f_score'][-l:]) - np.array(history['f_score'][-l:])).std()
    #     ])
    #
    #
    # sorted_keys = pandas.DataFrame(stats, columns=columns).sort_values(
    #     'loss', ascending=True
    # ).head(5).sort_values(
    #     'recall', ascending=True
    # ).head(4).sort_values(
    #     'precision', ascending=True
    # ).head(3).sort_values(
    #     'accuracy', ascending=True
    # ).head(2).sort_values(
    #     'f_score', ascending=True
    # ).head(1)['id']

    # df = df[df['id'].isin(sorted_keys)].sort_values('f_score', ascending=False)
    # df = df[df['id'] == int(sorted_keys)]
    # print(df)

    best = data.results[int(id)]

    draw(best['history'], [
        'accuracy',
        'precision',
        'recall',
        'auc',
        'f_score',
        'loss'
    ], 'best_nn')

    with open("data/trials/best_nn/space.json", "w") as f:
        f.write(str(best['space']))
    with open("data/trials/best_nn/metrics.json", "w") as f:
        json.dump(best['metrics'], f)


def neural_networks():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices --tf_xla_auto_jit=2 --tf_xla_cpu_global_jit'

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    import tensorflow as tf
    from tensorflow.keras import layers, models, optimizers, losses

    metrics = [
        'accuracy',
        'Precision',
        'Recall',
        'AUC'
    ]

    tf.compat.v1.enable_eager_execution()

    with open('data/trials/best_nn/space.json', 'r') as f:
        space = json.loads(
            str(f.read()).replace("'", '"').replace('None', 'null').replace('True', 'true').replace('False', 'false'))

    import tensorflow.keras.backend as K

    def f_score(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        recall = true_positives / (possible_positives + K.epsilon())
        f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
        return f1_val

    model = models.Sequential()

    layer = space['layers']

    while layer:
        model.add(layers.Dense(
            layer['nodes_count'],
            kernel_initializer=space['init'],
            activation=layer['activation'])
        )
        if layer['dropout']:
            model.add(layers.Dropout(layer['dropout']['dropout_rate'], trainable=space['trainable_dropouts']))
        if layer['BatchNormalization']:
            model.add(layers.BatchNormalization(trainable=space['trainable_BatchNormalization']))

        layer = layer['next']

    model.add(layers.Dense(1, kernel_initializer=space['init'], activation='sigmoid'))

    def scheduler(epoch, lr):
        return lr * tf.math.exp(-epoch / space['decay_steps'])

    def tf_callbacks():
        return [
            tf.keras.callbacks.ModelCheckpoint(
                'data/models/neural_networks_archSearch/tmp.h5',
                monitor='val_accuracy',
                mode='max',
                verbose=0,
                save_best_only=True
            ),
            tf.keras.callbacks.EarlyStopping(
                monitor='val_accuracy',
                patience=50,
                # min_delta=0.00001,
                mode='max',
                verbose=0),
            tf.keras.callbacks.LearningRateScheduler(scheduler)
        ]

    if space['optimizer']['type'] == 'Adadelta':
        optimizer = optimizers.Adadelta()
    elif space['optimizer']['type'] == 'Adagrad':
        optimizer = optimizers.Adagrad()
    elif space['optimizer']['type'] == 'Adam':
        optimizer = optimizers.Adam()
    elif space['optimizer']['type'] == 'Adamax':
        optimizer = optimizers.Adamax()
    elif space['optimizer']['type'] == 'Ftrl':
        optimizer = optimizers.Ftrl()
    elif space['optimizer']['type'] == 'Nadam':
        optimizer = optimizers.Nadam()
    elif space['optimizer']['type'] == 'RMSprop':
        optimizer = optimizers.RMSprop()
    elif space['optimizer']['type'] == 'SGD':
        optimizer = optimizers.SGD()

    optimizer.learning_rate = space['optimizer']['learning_rate']
    if 'amsgrad' in space['optimizer']:
        optimizer.amsgrad = space['optimizer']['amsgrad']
    if 'centered' in space['optimizer']:
        optimizer.centered = space['optimizer']['centered']
    if 'momentrum' in space['optimizer']:
        optimizer.momentum = space['optimizer']['momentum']
    if 'nesterov' in space['optimizer']:
        optimizer.nesterov = space['optimizer']['nesterov']

    model.compile(
        optimizer=optimizer,
        loss=losses.BinaryCrossentropy(from_logits=True),
        metrics=metrics + [f_score]
    )

    history = model.fit(
        x_train, y_train,
        validation_data=(x_test, y_test),
        # validation_split=0.1,
        epochs=1000,
        callbacks=tf_callbacks(),
        verbose=2,
        batch_size=space['batch_size'],
        shuffle=space['shuffle']
    )

    loss, accuracy, Precision, Recall, AUC, f_score = model.evaluate(x_test, y_test)

    m = {
        "loss": loss,
        "accuracy": accuracy,
        "Precision": Precision,
        "Recall": Recall,
        "AUC": AUC,
        "f_score": f_score
    }

    model.save("data/models/neural_networks/nn1.h5")
    with open("data/trials/neural_networks/history.pkl", 'wb') as f:
        pickle.dump(history.history, f)
    with open("data/trials/neural_networks/metrics.json", "w") as f:
        json.dump(m, f)

    print(m)
    draw(history.history, ['accuracy', 'precision', 'recall', 'auc', 'loss', 'f_score'], 'neural_networks')


def DT():
    from sklearn.tree import DecisionTreeClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/DT/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'criterion': hp.choice('criterion', ['gini', 'entropy']),
        'splitter': hp.choice('splitter', ['best', 'random']),
        'max_features': hp.choice('max_features', ['sqrt', 'log2', None]),
        'min_samples_split': 2,
        'min_samples_leaf': 1,
    }

    def objective(space):
        clf = DecisionTreeClassifier(
            criterion=space['criterion'],
            splitter=space['splitter'],
            max_features=space['max_features'],
            min_samples_leaf=space['min_samples_leaf'],
            min_samples_split=space['min_samples_split']
        )

        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        acc = accuracy_score(y_true=y_test, y_pred=y_pred)

        try:
            with open("data/trials/DT/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/DT/DT.pkl', 'wb'))
            with open("data/trials/DT/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/DT/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/DT/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=10 + len(trials),
        trials=trials,
        timeout=60 * 10
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/DT/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/DT/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def SVM():
    from sklearn.svm import SVC

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/SVM/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'C': hp.uniform('C', 0, 100000),
        'random_state': 42,
        'kernel': hp.choice('kernel', [
            {
                'type': 'linear',
            },
            {
                'type': 'poly',
                'degree': hp.randint('degree_poly', 360),
                'coef0': hp.uniform('coef0_poly', -10, 10)
            },
            {
                'type': 'rbf',
                'gamma': hp.choice('gamma_rbf', ['scale', 'auto'])
            },
            {
                'type': 'sigmoid',
                'gamma': hp.choice('gamma_sigmoid', ['scale', 'auto']),
                'coef0': hp.uniform('coef0_sigmoid', -10, 10)
            },
            {
                'type': 'precomputed',
                'gamma': hp.choice('gamma_precomputed', ['scale', 'auto'])
            }
        ]),
    }

    def objective(space):
        clf = SVC(
            C=space['C'],
            random_state=space['random_state'],
            kernel=space['kernel']['type'],
            max_iter=10000000,
            # tol=1e-2
        )

        if 'coef0' in space['kernel']:
            clf.coef0 = space['kernel']['coef0']
        if 'degree' in space['kernel']:
            clf.degree = space['kernel']['degree']
        if 'gamma' in space['kernel']:
            clf.gamma = space['kernel']['gamma']

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/SVM/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/SVM/SVM.pkl', 'wb'))
            with open("data/trials/SVM/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/SVM/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/SVM/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=50 + len(trials),
        trials=trials,
        timeout=60 * 10
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/SVM/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/SVM/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def KNN():
    from sklearn.neighbors import KNeighborsClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/kNN/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'k': hp.randint('k', 49) + 1,
        'p': hp.randint('p', 3) + 1,
        'weights': hp.choice('weights', ['uniform', 'distance']),
        'algorithm': hp.choice('algorithm', ['ball_tree', 'kd_tree', 'brute'])
    }

    def objective(space):
        clf = KNeighborsClassifier(
            n_neighbors=space['k'],
            p=space['p'],
            weights=space['weights'],
            algorithm=space['algorithm']
        )
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        acc = accuracy_score(y_true=y_test, y_pred=y_pred)

        try:
            with open("data/trials/kNN/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/kNN/{}NN.pkl'.format(space['k']), 'wb'))
            with open("data/trials/kNN/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/kNN/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/kNN/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=8 + len(trials),
        trials=trials,
        timeout=60 * 20 * 1
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/kNN/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/kNN/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def Gaussian_NB():
    from sklearn.naive_bayes import GaussianNB

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    clf = GaussianNB()
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_true=y_test, y_pred=y_pred)
    auc = roc_auc_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    m = {
        "accuracy": acc,
        "Precision": pre,
        "Recall": recall,
        "AUC": auc,
        "f_score": f_score
    }
    pickle.dump(clf, open('data/models/Gaussian_NB/Gaussian_NB.pkl', 'wb'))
    with open("data/trials/Gaussian_NB/metrics.json", "w") as f:
        json.dump(m, f)


def Bernoulli_NB():
    from sklearn.naive_bayes import BernoulliNB

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    clf = BernoulliNB()
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_true=y_test, y_pred=y_pred)
    auc = roc_auc_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    m = {
        "accuracy": acc,
        "Precision": pre,
        "Recall": recall,
        "AUC": auc,
        "f_score": f_score
    }
    pickle.dump(clf, open('data/models/Bernoulli_NB/Bernoulli_NB.pkl', 'wb'))
    with open("data/trials/Bernoulli_NB/metrics.json", "w") as f:
        json.dump(m, f)


def Complement_NB():
    from sklearn.naive_bayes import ComplementNB

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    clf = ComplementNB()
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_true=y_test, y_pred=y_pred)
    auc = roc_auc_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    m = {
        "accuracy": acc,
        "Precision": pre,
        "Recall": recall,
        "AUC": auc,
        "f_score": f_score
    }
    pickle.dump(clf, open('data/models/Complement_NB/Complement_NB.pkl', 'wb'))
    with open("data/trials/Complement_NB/metrics.json", "w") as f:
        json.dump(m, f)


def Multinomial_NB():
    from sklearn.naive_bayes import MultinomialNB

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    clf = MultinomialNB()
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_true=y_test, y_pred=y_pred)
    auc = roc_auc_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    m = {
        "accuracy": acc,
        "Precision": pre,
        "Recall": recall,
        "AUC": auc,
        "f_score": f_score
    }
    pickle.dump(clf, open('data/models/Multinomial_NB/Multinomial_NB.pkl', 'wb'))
    with open("data/trials/Multinomial_NB/metrics.json", "w") as f:
        json.dump(m, f)


# ansambles


def ET():
    from sklearn.ensemble import ExtraTreesClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/ET/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'n_estimators': hp.randint('n_estimators', 248) + 2,
        'criterion': hp.choice('criterion', ['gini', 'entropy']),
        'max_features': hp.choice('max_features', ['sqrt', 'log2', None]),
        'bootstrap': hp.choice('bootstrap', [False, True]),
        'oob_score': hp.choice('oob_score', [False, True]),
        'class_weight': hp.choice('class_weight', ['balanced', 'balanced_subsample', None]),
    }

    def objective(space):
        clf = ExtraTreesClassifier(
            n_estimators=space['n_estimators'],
            criterion=space['criterion'],
            max_features=space['max_features'],
            bootstrap=space['bootstrap'],
            oob_score=space['oob_score'],
            class_weight=space['class_weight']
        )

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/ET/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/ET/ET.pkl', 'wb'))
            with open("data/trials/ET/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/ET/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/ET/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=100 + len(trials),
        trials=trials,
        timeout=60 * 30
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/ET/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/ET/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def RF():
    from sklearn.ensemble import RandomForestClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/RF/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'n_estimators': hp.randint('n_estimators', 148) + 2,
        'criterion': hp.choice('criterion', ['gini', 'entropy']),
        'max_features': hp.choice('max_features', ['sqrt', 'log2']),
        'bootstrap': hp.choice('bootstrap', [False, True]),
        'oob_score': hp.choice('oob_score', [False, True]),
        'class_weight': hp.choice('class_weight', ['balanced', 'balanced_subsample', None]),
    }

    def objective(space):
        clf = RandomForestClassifier(
            n_estimators=space['n_estimators'],
            criterion=space['criterion'],
            max_features=space['max_features'],
            bootstrap=space['bootstrap'],
            oob_score=space['oob_score'],
            class_weight=space['class_weight']
        )

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/RF/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/RF/RF.pkl', 'wb'))
            with open("data/trials/RF/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/RF/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/RF/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=100 + len(trials),
        trials=trials,
        timeout=60 * 30
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/RF/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/RF/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def AdaBoost_DT():
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/AdaBoost_DT/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'n_estimators': hp.randint('n_estimators', 148) + 2,
        'learning_rate': hp.uniform('learning_rate', 0, 1),
        'algorithm': hp.choice('algorithm', ['SAMME', 'SAMME.R']),
        'max_depth': hp.randint('max_depth', 9)+1
    }

    def objective(space):
        clf = AdaBoostClassifier(
            DecisionTreeClassifier(max_depth=space['max_depth']),
            n_estimators=space['n_estimators'],
            learning_rate=space['learning_rate'],
            algorithm=space['algorithm']
        )

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/AdaBoost_DT/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/AdaBoost_DT/AdaBoost_DT.pkl', 'wb'))
            with open("data/trials/AdaBoost_DT/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/AdaBoost_DT/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/AdaBoost_DT/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=37 + len(trials),
        trials=trials,
        timeout=60 * 10
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/AdaBoost_DT/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/AdaBoost_DT/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def Bagging_DT():
    from sklearn.ensemble import BaggingClassifier
    from sklearn.tree import DecisionTreeClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/Bagging_DT/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'n_estimators': hp.randint('n_estimators', 148) + 2,
        'bootstrap_features': hp.choice('bootstrap_features', [False, True]),
        'max_depth': hp.randint('max_depth', 9)+1
    }

    def objective(space):
        clf = BaggingClassifier(
            DecisionTreeClassifier(max_depth=space['max_depth']),
            n_estimators=space['n_estimators'],
            bootstrap_features=space['bootstrap_features']
        )

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/Bagging_DT/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/Bagging_DT/Bagging_DT.pkl', 'wb'))
            with open("data/trials/Bagging_DT/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/Bagging_DT/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/Bagging_DT/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=100 + len(trials),
        trials=trials,
        timeout=60 * 30
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/Bagging_DT/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/Bagging_DT/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def GradientBoost():
    from sklearn.ensemble import GradientBoostingClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/GradientBoost/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'n_estimators': hp.randint('n_estimators', 148) + 2,
        'learning_rate': hp.uniform('learning_rate', 0, 1),
        'loss': hp.choice('loss', ['deviance', 'exponential']),
        'criterion': hp.choice('criterion', ['friedman_mse', 'mse']),
        'max_features': hp.choice('max_features', ['sqrt', 'log2', None])
    }

    def objective(space):
        clf = GradientBoostingClassifier(
            n_estimators=space['n_estimators'],
            learning_rate=space['learning_rate'],
            criterion=space['criterion'],
            max_features=space['max_features'],
            loss=space['loss']
        )

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/GradientBoost/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/GradientBoost/GradientBoost.pkl', 'wb'))
            with open("data/trials/GradientBoost/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/GradientBoost/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/GradientBoost/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=100 + len(trials),
        trials=trials,
        timeout=60 * 30
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/GradientBoost/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/GradientBoost/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


def HistGradientBoost():
    from sklearn.experimental import enable_hist_gradient_boosting
    from sklearn.ensemble import HistGradientBoostingClassifier

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    try:
        with open("data/trials/HistGradientBoost/results.pkl", 'rb') as file:
            trials = pickle.load(file)
    except:
        trials = Trials()

    space = {
        'learning_rate': hp.uniform('learning_rate', 0, 1),
        'loss': hp.choice('loss', ['auto', 'binary_crossentropy', 'categorical_crossentropy']),
    }

    def objective(space):
        clf = HistGradientBoostingClassifier(
            learning_rate=space['learning_rate'],
            loss=space['loss']
        )

        try:
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = accuracy_score(y_true=y_test, y_pred=y_pred)
        except:
            acc = -1

        try:
            with open("data/trials/HistGradientBoost/metric.txt") as f:
                max_acc = float(f.read().strip())  # read best metric,
        except FileNotFoundError:
            max_acc = -1

        if acc > max_acc:
            pickle.dump(clf, open('data/models/HistGradientBoost/HistGradientBoost.pkl', 'wb'))
            with open("data/trials/HistGradientBoost/space.json", "w") as f:
                f.write(str(space))
            with open("data/trials/HistGradientBoost/metric.txt", "w") as f:
                f.write(str(acc))

            auc = roc_auc_score(y_test, y_pred)
            f_score = f1_score(y_test, y_pred)
            pre = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            m = {
                "accuracy": acc,
                "Precision": pre,
                "Recall": recall,
                "AUC": auc,
                "f_score": f_score
            }
            with open("data/trials/HistGradientBoost/metrics.json", "w") as f:
                json.dump(m, f)

        return {'loss': -acc, 'status': STATUS_OK, 'space': space}

    best = fmin(
        objective,
        space,
        algo=tpe.suggest,
        max_evals=100 + len(trials),
        trials=trials,
        timeout=60 * 10
    )

    def typer(o):
        if isinstance(o, np.int32): return int(o)
        return o

    with open("data/trials/HistGradientBoost/best.json", "w") as f:
        json.dump(best, f, default=typer)

    with open("data/trials/HistGradientBoost/results.pkl", 'wb') as output:
        pickle.dump(trials, output)


# summary
# - Stacking


def Stacking():
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    from sklearn.experimental import enable_hist_gradient_boosting
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.ensemble import BaggingClassifier

    from sklearn.svm import SVC
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.naive_bayes import BernoulliNB
    from sklearn.naive_bayes import ComplementNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.neighbors import KNeighborsClassifier

    from sklearn.linear_model import LogisticRegression

    from sklearn.ensemble import StackingClassifier

    estimators = [
        ('SVM', SVC(
            C=15441.43371319063,
            random_state=42,
            kernel='rbf',
            gamma='auto',
            max_iter=1000000,
        )),
        ('GNB', GaussianNB()),
        ('BNB', BernoulliNB()),
        ('CNB', ComplementNB()),
        ('MNB', MultinomialNB()),
        ('RF', RandomForestClassifier(
            class_weight='balanced_subsample',
            n_estimators=102,
            max_features='log2',
            bootstrap=False,
            oob_score=False
        )),
        ('HGBC', HistGradientBoostingClassifier(
            learning_rate=0.2776671879915404
        )),
        ('GBC', GradientBoostingClassifier(
            learning_rate=0.447268184247265,
            loss='exponential',
            n_estimators=944,
            criterion='mse',
            max_features=None
        )),
        ('AdaBoost_DT', AdaBoostClassifier(
            DecisionTreeClassifier(max_depth=9),
            n_estimators=113,
            learning_rate=0.6844446777168631,
            algorithm='SAMME'
        )),
        ('kNN', KNeighborsClassifier(
            algorithm='kd_tree',
            weights='distance',
            n_neighbors=12,
            p=1
        )),
        ('ET', ExtraTreesClassifier(
            n_estimators=185,
            max_features=None
        )),
        ('DT', DecisionTreeClassifier(
            criterion='entropy',
            max_features=None
        )),
        ('Bagging_DT', BaggingClassifier(
            DecisionTreeClassifier(max_depth=9),
            n_estimators=119,
            bootstrap_features=True
        ))
    ]

    clf = StackingClassifier(
        estimators=estimators,
        final_estimator=LogisticRegression(),
        stack_method='predict',
        verbose=2,
        n_jobs=3
    )

    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_true=y_test, y_pred=y_pred)

    pickle.dump(clf, open('data/models/Stacking (All)/StackingClassifier.pkl', 'wb'))

    auc = roc_auc_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    m = {
        "accuracy": acc,
        "Precision": pre,
        "Recall": recall,
        "AUC": auc,
        "f_score": f_score
    }
    with open("data/trials/Stacking (All)/metrics.json", "w") as f:
        json.dump(m, f)

