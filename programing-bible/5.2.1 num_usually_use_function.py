# 數值函式整理

# 取得 x 的絕對值 abs(x)
absolute_value = abs(-5)
print(absolute_value) # 5

# 取得整數 x 的字元 chr(x)
num_convert_chr = chr(65)
print(num_convert_chr) # A

# 取得 x 除以 y 的商及餘數的元組 divmod(x, y)
div_mod = divmod(44, 6) # 44 / 6 = 7...2
print(div_mod) # (7, 2)

# 將 x 轉換成浮點數 float(x)
float_value = float("56")
print(float_value) # 56.0

# 將 x 轉換成十六進位數字 hex(x)
hex_value = hex(34)
print(hex_value) # 0x22

# 將 x 轉換成整數 int(x)
int_value = int(34.21)
print(int_value) # 34

# 取得元素個數 len(x)
len_value = len([1, 2, 3, 4])
print(len_value) # 4

# 取得參數串列中的最大值 max(參數串列)
max_value = max(1, 3, 5, 7)
print(max_value) # 7

# 取得參數串列中的最小值 min(參數串列)
min_value = min(1, 3, 5, 7)
print(min_value) # 1

# 將 x 轉換成八進位數字 oct(x)
oct_value = oct(34)
print(oct_value) # 0o42

# 回傳字元 x 的 Unicode 編碼值 ord(x)
ord_value = ord("我")
print(ord_value) # 25105

# 取得 x 的 y 次方 pow(x, y)
pow_value = pow(2, 3)
print(pow_value) # 8

# 以四捨五入法取得 x 的近似值 round(x)
round_value = round(45.8)
print(round_value) # 46

# 由小到大排序 sorted(串列)
sorted_value = sorted([3, 1, 7, 5])
print(sorted_value) # [1, 3, 5, 7]

# 將 x 轉換成字串 str(x)
str_value = str(56)
print(str_value) # 56

# 計算串列元素的總和 sum(串列)
sum_value = sum([1, 3, 5, 7])
print(sum_value) # 16
