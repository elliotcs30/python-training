# 數字和句點搜尋
# 以 ^/d+ 搜尋數字開始的所有字元，以 w+$ 搜尋結束為數字、字母或底線字元的所有字元。

import re
pat = r'^\d+'
s = "2020 is coming soon"
m = re.findall(pat, s)
print(m) # ['2020']
m2 = re.findall(r'\w+$', s)
print(m2) # ['soon']