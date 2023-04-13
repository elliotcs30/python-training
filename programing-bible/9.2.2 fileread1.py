# 開啟 file1.txt 文字檔為讀取模式，並顯示資料內容。

f = open('file1.txt', 'rt')
for line in f:
    print(line, end="")
f.close()

# Hello Python
# 中文字測試
# Welcome