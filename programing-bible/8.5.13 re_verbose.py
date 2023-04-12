# 正規表達式中加上註解
# 以 re.VERBOSE 參數為正規表達式加上註解。

import re
pat = r'.*'
s = "Do your best,\nGo Go Go!"
m = re.search(pat, s)
print(m.group()) # Do your best,

m2 = re.search(r'.*', s, re.DOTALL)
print(m2.group()) # Do your best,\nGo Go Go!