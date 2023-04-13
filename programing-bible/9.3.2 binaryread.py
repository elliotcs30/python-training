# 讀取二進位檔案
# 開啟 file.bin 二進位檔為讀取模式，並顯示讀取的資料。

with open('file.bin', 'rb') as f:
    content = f.read().decode("utf-8")
    print(content)