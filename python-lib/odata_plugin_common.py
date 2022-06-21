try:
    from urllib.parse import urlparse, parse_qs, urlunsplit
except:
    from urlparse import urlparse, parse_qs, urlunsplit


def split_params_from_url(url):
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    url_without_querystring = urlunsplit([parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', ''])
    return params, url_without_querystring
