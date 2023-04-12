# 在 try 敘述中顯示 n，但因為變數 n 並不存在，
# 執行時將會引發例外，執行 except 中的程式區塊，因此會顯示「變數 n 不存在!」訊息。

try:
    print(n)
except:
    print("變數 n 不存在!")