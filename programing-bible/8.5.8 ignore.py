# 忽略大小寫搜尋
# 不分大小寫搜尋 PYTHON 和 ANDROID 字串。

import re
pat = r'PYTHON|ANDROID'
s = "I like Python and Android"
m = re.findall(pat, s, re.I)
print(m) # ['Python', 'Android]