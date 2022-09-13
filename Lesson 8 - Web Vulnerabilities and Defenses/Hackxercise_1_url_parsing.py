"""
Implement a function that given a URL, parses it and returns a tuple with its protocol, domain and path.
For example, for "http://www.google.com/search", it whould return ('http', 'www.google.com', '/search').

"""
# imports go here
from urllib.parse import urlparse

def parse_url(url):
     url_parsed = urlparse(url)
     return url_parsed.scheme, url_parsed.netloc, url_parsed.path
