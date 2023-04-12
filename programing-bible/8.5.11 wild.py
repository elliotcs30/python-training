# .和.*搜尋
# 以 .o 和 .*o 搜尋字串中，2個及2個字元以上，並且以 o 字元結尾的所有字串。

import re
pat = r'.o'
s = "Do your best!"
m = re.findall(pat, s)
print(m) # ['Do', 'yo']

m2 = re.findall(r'.*o', s)
print(m2) # ['Do', 'yo']