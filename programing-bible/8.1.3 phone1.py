# 小括號分組練習
# 用小括號和「-」字元將電話號碼分成兩組，第一組是兩個數字、第二組是八個數字。

import re
numStr = "tel:04-12345678"
pat = r'(\d{2})-(\d{8})'

phone = re.search(pat, numStr)
if not phone==None:
    print(phone.group())    # 04-12345678
    print(phone.group(0))   # 04-12345678
    print(phone.group(1))   # 04
    print(phone.group(2))   # 04-12345678