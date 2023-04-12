# 使用 ? 字元搜尋「-」字元
# 利用小括號將電話號碼分成兩組，第一組的區域號碼中包含「()」符號，區域號碼和電話號碼間的「-」字元可有可無。

import re
phoneList = ["(04)12345678", "(04)-12345678"]

pat = r'(\(\d{2}\))-?(\d{8})'

for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())