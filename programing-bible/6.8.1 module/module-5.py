# 匯入模組所有函式
# 風險: 每一個模組擁有眾多函式，若兩個模組有相同名稱的函式，由於未輸入模組名稱，使用函式時將會造成錯誤。
from calculate import *

print(add(5, 2)) # 7
print(sub(5, 2)) # 3