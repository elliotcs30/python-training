# 使用 + 字元搜尋
# 以「+」字元搜尋字串中所有的小寫英文字母。

import re
pat = re.compile(r'[aeiou]+')
s = "John is my best friend."
m = re.findall(pat, s)
print(m) # ['o', 'i', 'e', 'ie']