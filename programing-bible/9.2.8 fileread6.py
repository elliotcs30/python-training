# 讀取 UTF-8 編碼的 file1.txt 檔案的文件內容
with open('file1.txt', 'r', encoding='UTF-8') as f:
    doc = f.readlines()
    print(doc) # ['\ufeff123中文字\n', 'abcde\n', 'hello\n']

with open('file1.txt', 'r', encoding='UTF-8') as f:
    str1 = f.read(5)
    print(str1) # 123 中