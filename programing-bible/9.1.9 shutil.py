# 複製  shutil.py 為 newfile.py 及 D:\new.py

import os, shutil
cur_path = os.path.dirname(__file__) # 取得目前路徑
destfile = f"{cur_path}\\newfile.py"
shutil.copy("shutil.py", destfile)   # 檔案複製
shutil.copyfile("shutil.py", "D:\\new.py") # 檔案複製