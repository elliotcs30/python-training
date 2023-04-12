# 使用 | 字元搜尋
# 利用「|」同時搜尋多種格式的電話號碼。

import re
phoneList = ["0412345678", "(04)12345678", "(04)-12345678", "(049)2987654", "0937-998877"]

pat = r'\(\d{2,4}\)-?\d{6,8}|\{9,10}|\d{4}-\d{6,8}'
for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group()) # (04)12345678、(04)-12345678、(049)2987654、0937-998877