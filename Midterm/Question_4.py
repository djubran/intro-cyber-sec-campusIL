"""
The fetch(url) function fetches a page from the web. To avoid re-fetching the same pages twice, which is pretty slow, it caches them per user (it figures out the current user by looking at os.environ['USER']). Here's its implementation:

_cache = {}
def fetch(url):
    user = os.environ['USER']
    if user not in _cache:
        _cache[user] = {}
    if url not in _cache[user]:
        _cache[user][url] = requests.get(url).content
    return _cache[user][url]
Write a function, did_fetch(user, url), that figures out whether some user has fetched some url or not. You can assume fetching a resource from the web takes at least 0.1 seconds, while fetching it from the cache is near immediate

"""


import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.fetch import fetch
import time
import os

def did_fetch(user, url):
    flag = True
    os.environ['USER'] = user
    start = time.time()
    fetch(url)
    end = time.time()
    elapsed_time = end - start
    print(elapsed_time)
    if elapsed_time >= 0.1:
        flag =  False
    return flag
