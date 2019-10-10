from urllib.request import urlopen
from bs4 import *
from SafeSpider import getTitle

text = urlopen("https://www.zhihu.com")
bsobj = BeautifulSoup(text.read(),"html.parser")
print(bsobj.__unicode__() )
print(getTitle("https://www.zhihu.com"))
