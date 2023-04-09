# 以字串排版函式列印成績單
# 一年五班有三位同學，請設計程式幫老師以rjust、ljust函式整齊列印出班級成績單。

list_name = ["張同學", "許同學", "陳同學"]
list_chinese = [100, 90, 88]
list_math = [100, 95, 72]
list_english = [100, 92, 69]
print("姓名     座號   國文   數學   英文")
for i in range(0, 3):
    print(list_name[i].ljust(5), str(i+1).rjust(2),
          str(list_chinese[i]).rjust(7), 
          str(list_math[i]).rjust(6),
          str(list_english[i]).rjust(6))