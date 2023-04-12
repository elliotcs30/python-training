# 同時捕捉非數值資料和除數為 0 的錯誤
# 輸入兩個正整數，求兩數之餘數時，並以 try...except 同時捕捉輸入非數值資料和除數為 0 的錯誤。

# AttributeError: 物件無此屬性
# Exception: 所有的錯誤
# FileNotFoundError: open() 開啟檔案時找不到檔案的錯誤
# IOError: 輸入/輸出錯誤
# IndexError: 索引超出範圍
# MemoryError: 記憶體空間不足
# NameError: 變數名稱未宣告的錯誤
# SyntaxError: 語法錯誤
# TypeError: 資料型別的錯誤
# ValueError: 傳入無效的參數，產生數值錯誤
# ZeroDivisionError: 除數為 0 的錯誤

try:
    a = int(input("請輸入第一個整數:"))
    b = int(input("請輸入第二個整數:"))
    result = a / b
except (VslueError, ZeroDivisionError):
    print("發生輸入非數值的錯誤或分母為 0 的錯誤!")
else:
    print("result =", result)