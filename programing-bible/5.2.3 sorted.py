# 電費統計及排序

# 設計程式輸入電費，若輸入「 -1 」表示輸入資料結束，使用內建函式顯示最多電費、最少電費、電費總和及將電費由大到小排序。

input_evl = 0
evl_list = []

while(input_evl != -1):
    input_evl = int(input("請輸入點費 (-1: 結束)："))
    evl_list.append(input_evl)
evl_list.pop() 

print(f"共輸入 {len(evl_list)} 個數")
print(f"最多電費為： {max(evl_list)}")
print(f"最少電費為： {min(evl_list)}")
print(f"電費總和為： {sum(evl_list)}")
print(f"電費由大到小排序為： {sorted(evl_list)}")