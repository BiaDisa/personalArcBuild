import urllib

import requests
import re
from urllib.robotparser import RobotFileParser

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-.*?.*?>(.*?)</a>', re.S)
##print(r.text)

rp = urllib.robotparser.RobotFileParser(url='https://www.zhihu.com/robots.txt')
rp.read()
##print(rp.can_fetch('*','www.zhihu.com'))

str = 'https://api.weixin.qq.com/card/invoice/getauthurl?access_token=26_rPrSFwuHq12XDR4wubI2maJ1fwQdq7SlOyqXSXtoj9GEUJZD3Q6dQS1VdlB3VY9Ac4VQjsUs9Ehv3F9uufV8viVowi5RsszFk_YJSkbHE5AvAxx0CqTMvzGpX_rAwskztGGh3fuMIUuSLUauKOGaAJAFJB'
print(re.after("access_token", str))