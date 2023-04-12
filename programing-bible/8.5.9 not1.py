# 數字和句點搜尋
# 以[^a-z.]+ 搜尋 a-z. 和空白字元以外的所有字元。

import re
pat = r'[^a-z. ]+'

s = 'John was 18 year old.'
m = re.findall(pat, s)
print(m) # ['J', '18']