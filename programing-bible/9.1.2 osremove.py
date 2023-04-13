# 刪除指定的檔案，一般都會配合 os.path 的 exists 函式，先檢查該檔案是否存在，再決定是否要刪除檔案。

import os

file = "myFile.txt"

if os.path.exists(file):
    os.remove(file)
else:
    print(f"{file}檔案未建立!")