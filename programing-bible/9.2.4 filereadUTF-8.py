# 使用 cp950 開啟已另存為 UTF-8 編碼格式 file2.txt 檔並顯示資料內容

f = open('file1.txt', 'r', encoding='cp950') # UTF-8
for line in f:
    print(line, end="")
f.close()