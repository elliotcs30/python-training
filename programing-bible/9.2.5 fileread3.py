# read 會從目前的指標的位置，讀取指定長度的字元，如果未指定長度則會讀取所有的字元。
# 讀取 file1.txt 檔案的前 5 個字元。

with open("file1.txt", 'r') as f:
    str1 = f.read(5)
    print(str1) # Hello