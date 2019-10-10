from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except(HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsobj = BeautifulSoup(html.read(), "html.parser")
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title
