# 數字和句點搜尋
# 以 [0-9+]+ 搜尋字串中所有的數字和加號。

import re
pat = r'[0-9+]+'
s = "Amy was 18 years old, she likes Python and C++."
m = re.findall(pat, s)
print(m) # ['18', '++']