# 開啟 file.bin 二進位檔為讀取模式，配合 seek 函式讀取指定的資料。

# file.bin 內容
'''Hello world
中文字測試
Welcome
'''

f = open('file.bin', 'rb')
print(f"目前文件索引位置:", f.tell()) # 0

f.seek(6) # 移到索引第 6 (第 7 個字元) 位置
str1 = f.read(7) # 讀取第 7 個字元
print(str1)      # b'Python\n'
print("目前文件索引位置:", f.tell()) # 13

f.seek(0) # 回文件最前端
print("目前文件索引位置:", f.tell()) # 0
str2 = f.read(5) # 讀取 5 個字元
print(str2) # b'Hello'

f.seek(-8, 2) # 移至最尾端，向前取 8 個字元
str3 = f.read()
print(str3) # b'Welcome\n'

f.close()