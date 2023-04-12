# 行動電話號碼格式檢查
# 判斷行動電話號碼是否是台灣行動電話的號碼。

def isTaiwanPhone(str):
    if len(str) != 11:          # 如果長度不是 11
        return False            # 傳回非手機號碼格式
    
    # 檢查 11 個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != '-':   # 如果第 5 個字元不是 '-' 字元
                return False    # 傳回非手機號碼格式
            else:               # 如果前 4 個字或最後 6 個字出現非數字字元
                if str[i].isdecimal() == False:
                    return False # 傳回非手機號碼格式
    return True                  # 傳回是正確手機號碼格式

print(f"0937-123456 是台灣手機號碼: {isTaiwanPhone('0937-123456')}")
print(f"02-12345678 是台灣手機號碼: {isTaiwanPhone('02-12345678')}")