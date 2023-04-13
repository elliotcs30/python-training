# 利用 mkdir 函式可以建立指定的目錄。

import os

dir = "myDir"

if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(f"{dir}已經建立!")