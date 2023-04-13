# 寫入二進位檔案
# 開啟 file.bin 二進位檔為寫入模式，並將資料寫入檔案中。

content = '''Hello Python
中文字測試
Welcome
'''

content = content.encode("utf-8") # 轉成 bytes
with open('file.bin', 'wb') as f:
    f.write(content)