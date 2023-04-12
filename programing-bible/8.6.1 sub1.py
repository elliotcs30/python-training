# 將 "Password:1234, ID:5678" 字串中數字密碼和 ID 號碼都以 * 字元替換，即 "Password:*,ID:*"。

import re
pat = r"\d+"
substr = "*"
s = "Password:1234, ID:5678"
result = re.sub(pat, substr, s)
print(result) # Password:*, ID:*