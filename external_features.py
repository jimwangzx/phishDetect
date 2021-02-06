from datetime import datetime
from bs4 import BeautifulSoup
import requests
import whois
import time
from tools import benchmark
import re


OPR_key = open("OPR_key.txt").read()


########################################################################################################################
#               Domain registration age
########################################################################################################################

@benchmark
def domain_registration_length(domain):
    try:
        res = whois.whois(domain)
        expiration_date = res.expiration_date
        today = time.strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d')
        # Some domains do not have expiration dates. The application should not raise an error if this is the case.
        if expiration_date:
            if type(expiration_date) == list:
                expiration_date = min(expiration_date)
            return abs((expiration_date - today).days)
        else:
            return 0
    except:
        return -1


#################################################################################################################################
#               Domain recognized by WHOIS
#################################################################################################################################

@benchmark
def whois_registered_domain(domain):
    try:
        hostname = whois.whois(domain).domain_name
        if type(hostname) == list:
            for host in hostname:
                if re.search(host.lower(), domain):
                    return 1
            return 0
        else:
            if re.search(hostname.lower(), domain):
                return 1
            else:
                return 0
    except:
        return -1


#################################################################################################################################
#               Unable to get web traffic (Page Rank)
#################################################################################################################################


import sys, lxml

@benchmark
def web_traffic(short_url):
    try:
        rank = BeautifulSoup(requests("http://data.alexa.com/data?cli=10&dat=s&url=" + short_url).text,
                             "xml").find("REACH")['RANK']
    except:
        return -1

    # return min(int(rank), 10000000)
    return rank


#################################################################################################################################
#               Domain age of a url
#################################################################################################################################

import json

@benchmark
def domain_age(domain):
    url = domain.split("//")[-1].split("/")[0].split('?')[0]
    show = "https://input.payapi.io/v1/api/fraud/domain/age/" + url
    r = requests.get(show)

    if r.status_code == 200:
        data = r.text
        jsonToPython = json.loads(data)
        result = jsonToPython['result']
        if result == None:
            return -2
        else:
            return result
    else:
        return -1


#################################################################################################################################
#               Google index
#################################################################################################################################


from urllib.parse import urlencode

@benchmark
def google_index(url):
    # time.sleep(.6)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    query = {'q': 'site:' + url}
    google = "https://www.google.com/search?" + urlencode(query)
    data = requests.get(google, headers=headers)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")
    try:
        if 'Our systems have detected unusual traffic from your computer network.' in str(soup):
            return -1
        check = soup.find(id="rso").find("div").find("div").find("a")
        if check and check['href']:
            return 1
        else:
            return 0

    except AttributeError:
        return -1


########################################################################################################################
#               Page Rank from OPR
########################################################################################################################


def http_build_query(params, topkey=''):
    from urllib.parse import quote

    if len(params) == 0:
        return ""

    result = ""

    # is a dictionary?
    if type(params) is dict:
        for key in params.keys():
            newkey = quote(key)
            if topkey != '':
                newkey = topkey + quote('[' + key + ']')

            if type(params[key]) is dict:
                result += http_build_query(params[key], newkey)

            elif type(params[key]) is list:
                i = 0
                for val in params[key]:
                    result += newkey + quote('[' + str(i) + ']') + "=" + quote(str(val)) + "&"
                    i = i + 1

            # boolean should have special treatment as well
            elif type(params[key]) is bool:
                result += newkey + "=" + quote(str(int(params[key]))) + "&"

            # assume string (integers and floats work well)
            else:
                result += newkey + "=" + quote(str(params[key])) + "&"

    # remove the last '&'
    if (result) and (topkey == '') and (result[-1] == '&'):
        result = result[:-1]

    return result


@benchmark
def page_rank(domains):
    url = 'https://openpagerank.com/api/v1.0/getPageRank?' + http_build_query({"domains": domains})
    try:
        request = requests.get(url, headers={'API-OPR': OPR_key})
        result = request.json()
        result = [record['page_rank_decimal'] for record in result['response']]
        return result
    except:
        return None


########################################################################################################################
#               Google search by keywords
########################################################################################################################


from googlesearch import search

@benchmark
def compare_search2url(url, domain, keywords):
    return search("http://{0}={1}".format(domain, '+'.join(keywords), 0))[0] == url


########################################################################################################################
#               Certificate information
########################################################################################################################


from OpenSSL import SSL
from cryptography import x509
import idna

from socket import socket
from collections import namedtuple

HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')


def get_hostinfo(hostname, port):
    try:
        hostname_idna = idna.encode(hostname)
        sock = socket()

        sock.connect((hostname, port))
        peername = sock.getpeername()
        ctx = SSL.Context(SSL.SSLv23_METHOD) # most compatible
        ctx.check_hostname = False
        ctx.verify_mode = SSL.VERIFY_NONE

        sock_ssl = SSL.Connection(ctx, sock)
        sock_ssl.set_connect_state()
        sock_ssl.set_tlsext_host_name(hostname_idna)
        sock_ssl.do_handshake()
        cert = sock_ssl.get_peer_certificate()
        crypto_cert = cert.to_cryptography()
        sock_ssl.close()
        sock.close()

        return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)
    except:
        return HostInfo


def get_alt_names(cert):
    try:
        ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        return ext.value.get_values_for_type(x509.DNSName)
    except x509.ExtensionNotFound:
        return None

@benchmark
def count_alt_names(cert):
    try:
        return len(get_alt_names(cert))
    except:
        return -1

@benchmark
def valid_cert_period(cert):
    try:
        return (cert.not_valid_after - cert.not_valid_before).days
    except:
        return -1

@benchmark
def remainder_valid_cert(cert):
    try:
        period = cert.not_valid_after - cert.not_valid_before

        today = time.strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d')

        passed_time = today - cert.not_valid_before

        return max(0, min(1, passed_time / period))
    except:
        return -1
