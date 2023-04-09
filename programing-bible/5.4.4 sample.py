# 大樂透中獎號碼
# 大樂透中獎號碼為 6 個 1 到 49 之間的數字加 1 個特別號:
# 撰寫程式取得大樂透中獎號碼，並由小到大顯示方便對獎。

import random as r

list = r.sample(range(1, 50), 7)
special = list.pop()
list.sort()

print(f"本期大樂透中獎號碼為:", end=" ")
for i in range(0, len(list)):
    if i == 5:
        print(str(list[i]))
    else:
        print(str(list[i]), end=", ")

print(f"本期大樂透特別號為: {str(special)}")