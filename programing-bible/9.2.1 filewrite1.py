# 開啟 file1.txt 文字檔為寫入模式，並將資料寫入檔案中。

content = '''Hello Python
中文字測試
Welcome
'''

f = open('file1.txt', 'w')
f.write(content)
f.close()