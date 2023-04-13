# os.walk 可以搜尋指定目錄以及其子目錄，會傳回一個包含 3 個元素的元組，
# 分別是目錄名稱(dirname)、下一層目錄串列(subdir)、和目前中所有檔案串列(files)。

import os

cur_path = os.path.dirname(__file__) # 取得目前路徑

sample_tree = os.walk(cur_path)

for dirname, subdir, files, in sample_tree:
    print(f"檔案路徑: {dirname}") # 檔案路徑: .
    print(f"目錄串列: {subdir}")  # 目錄串列: []
    print(f"檔案串列: {files}")   # 檔案串列: ['oswalk.py', 'oswalk1.txt']
    print()