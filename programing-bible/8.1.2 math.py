# 正規表達式
import re
pat = re.compile(r'[a-z]+')

m = pat.match('tem12po')
print(m) # <re.Match object; span=(0, 3), match='tem'>

s = pat.search('tem12po')
print(s) # <re.Match object; span=(0, 3), match='tem'>

f = pat.findall('tem12po')
print(f) # ['tem', 'po']