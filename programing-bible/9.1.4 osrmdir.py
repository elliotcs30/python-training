# rmdir 函式可以刪除指定的目錄，刪除目錄前必須先刪除該目錄的檔案。
# 一班都會先檢查該目錄是否已經建立，再決定是否要刪除目錄。

import os

dir = "myDir"

if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(f"{dir}目錄未建立!")