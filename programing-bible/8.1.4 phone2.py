# 區域號碼中加入小括號
# 利用小括號將電話號碼分成兩組，第一組的區域號碼中包含「()」符號。

import re
numStr = "tel:(04)12345678"
pat = r'(\(\d{2}\))(\d{8})'

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())    # (04)12345678
    print(phone.group(1))   # (04)
    print(phone.group(2))   # 12345678