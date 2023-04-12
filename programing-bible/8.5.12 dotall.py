# 跳列字元的處理
# 使用和不使用第 3 個參數 re.DOTALL 忽略換列字元搜尋的比較。

import re
pat = r'.*'
s = "Do your best, \nGo Go Go!"
m = re.search(pat, s)
print(m.group()) # Do your best,

m2 = re.search(r'.*', s, re.DOTALL)
print(m2.group()) # Do your best,\nGo Go Go!