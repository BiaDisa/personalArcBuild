import json
import time

import requests
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


def get_one_page(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile("<dd>.*?board-index.*?>(.*?)</i>"
                         ".*?data-src=\"(.*?)\".*?alt=\"(.*?)\""
                         ".*?star.*?>(.*?)</p>"
                         ".*?releasetime.*?>(.*?)</p>"
                         ".*?integer.*?>(.*?)</i>"
                         ".*?fraction.*?>(.*?)</i>", re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file_as_json(content, local_url) :
    with open(local_url, 'ab+') as file: # a:append,w:write,r:read  t:text,b:byte
        print(type(json.dumps(content)))
        file.write(json.dumps(content, ensure_ascii=False,).encode('utf-8'))


def main():
    urlBase = 'https://maoyan.com/board/4?offset='
    i = 0
    while i <= 90:
        url = urlBase + i.__str__()
        html = get_one_page(url)
        if html is not None:
            colletion = parse_one_page(html)
            for item in colletion :
                write_to_file_as_json(item, 'maoyanTop100Json.txt')
            time.sleep(0.1)
        i = i + 10


main()