# 讀取 UTF-8 編碼的 file1.txt

with open('file2.txt', 'r', encoding='UTF-8') as f:
    print(f.readline())  # 123 中文字 \n
    print(f.readline(3)) # abc