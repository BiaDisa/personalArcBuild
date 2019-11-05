import re
from typing import List

print("start")
plainContent = 'Chapter 100'
content = '<H1>Chapter 1 - 介绍正则表达式</H1>'
sor = "Is is the cost of of gasoline going up up"
result2 = re.match('^Chapter [1-9][0-9]?', plainContent)
print(re.fullmatch("\b([a-z]+) \1\b/ig", sor))
if result2 is not None:
    print(result2.string)
result: List[str] = re.split('<.*?>', content)

print(result)

