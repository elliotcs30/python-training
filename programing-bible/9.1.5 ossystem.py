# 執行作業系統命令

import os

cur_path = os.getcwd()  # 取得目前路徑
os.system("cls")        # 清除螢幕
os.system("mkdir dir2") # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案
file = f"{cur_path}\dir2\copyfile.py"
os.system(f"notepad {file}") # 以記事本開啟 copyfile.py 檔
