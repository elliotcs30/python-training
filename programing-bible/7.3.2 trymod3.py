# 同時顯示非數值資料和除數為 0 內建的錯誤訊息
# 輸入兩個正整數，求兩數之餘數時，並以 try...except...as e 同時捕捉輸入非數值資料和除數為 0 內建的錯誤訊息。

try:
    a = int(input("請輸入第一個整數:"))
    b = int(input("請輸入第二個整數:"))
    r = a / b
except (ValueError, ZeroDivisionError) as e:
    print(f"發生 {e} 的錯誤!")
else:
    print("r =", r)