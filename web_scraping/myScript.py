from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        title = bsObj.body.div
    except ArithmeticError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
