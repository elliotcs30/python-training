# 使用 with 結束後會自動關閉開啟的檔案

with open('file1.txt', 'r') as f:
    for line in f:
        print(line, end="")
