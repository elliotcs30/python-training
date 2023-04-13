# 讀取全部文件內容，會以串列方式傳回，每一列會成為串列中的一個元素。
# 讀取 file1.txt 檔案的所有文件內容。

with open('file1.txt', 'r') as f:
    content = f.readlines()
    print(type(content)) # <class 'list'>
    print(content)