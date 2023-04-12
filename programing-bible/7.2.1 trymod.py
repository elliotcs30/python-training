# 捕捉非數值資料和除數為 0 的錯誤
# 輸入兩個正整數，求兩數之餘數時，並以 try...except 捕捉發生的例外，包括輸入非數值資料和除數為 0 的例外。

try:
    a = int(input("請輸入第一個整數:"))
    b = int(input("請輸入第二個整數:"))
    result = a % b
except ValueError:
    print("發生輸入非數值的錯誤!")
except Exception as e:
    print(f"發生 {e} 的錯誤，包括分母為 0 的錯誤!")
else:
    print("result =", result)
finally:
    print("一定會執行的程式區塊")