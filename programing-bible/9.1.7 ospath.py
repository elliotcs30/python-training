# join 函式可以將參數內的字串結合成一個檔案路徑，參數可以 2 個或 2 個以上。
# 取得最後的檔案或路徑名稱、目前檔案目錄路徑、偵測是否為目錄、將路徑分解為路徑和檔名、取得磁碟機名稱以及檔案路徑結合等。

import os

filename = os.path.abspath("9.1.7 ospath.py")

if os.path.exists(filename):
    basename = os.path.basename(filename)
    print(f"最後的檔案或路徑名稱: {basename}")      # 最後的檔案或路徑名稱: 9.1.7 ospath.py
    
    dirname = os.path.dirname(filename)
    print(f"目前檔案目錄路徑: {dirname}")           # 目前檔案目錄路徑: C:\...\...\Doc...\Git...\python-training\programing-bible
    
    print(f"是否為目錄: {os.path.isdir(filename)}") # 是否為目錄: False
    
    fullpath, fname = os.path.split(filename)
    print(f"目錄路徑: {fullpath}")                  # 目錄路徑: C:\...\...\Doc...\Git...\python-training\programing-bible
    print(f"檔名: {fname}")                         # 檔名: 9.1.7 ospath.py
    
    Drive, fpath = os.path.splitdrive(filename)
    print(f"磁碟機: {Drive}")                       # 磁碟機: C:

    print(f"路徑名稱: {fpath}")                     # 路徑名稱: \...\...\Doc...\Git...\python-training\programing-bible\9.1.7 ospath.py

    
    fullpath = os.path.join(fullpath, fname)
    print(f"組合路徑 = {fullpath}")                 # 組合路徑 = C:\...\...\Doc...\Git...\python-training\programing-bible\9.1.7 ospath.py