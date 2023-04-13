# glob 模組

# 取得 glob.py 檔、檔名前兩個字元是 os 開頭的所有 py 檔案以及所有副檔名為 txt 的檔案。

import glob

files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt")

for file in files:
    print(file) # demo.txt、err.txt