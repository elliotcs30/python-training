# os.path 模組

# abspath(): 傳回檔案完整的路徑名稱。
# basename(): 傳回檔案路徑名稱最後的檔案或路徑名稱。如果測試的是檔案會傳回檔名，測試的是路徑會傳回路徑。
# dirname(): 傳回指定檔案完整的目錄路徑，dirname(__file__)則可以取得目前的目錄路徑。
# exists(): 檢查指定的檔案或路徑是否存在。
# getsize(): 取得指定檔案的大小 (Bytes)。
# isabs(): 檢查指定路徑是否為完整路徑名稱。
# isfile(): 檢查指定路徑是否為檔案。
# isdir(): 檢查指定路徑是否為目錄。
# split(): 分割檔案路徑名稱為目錄路徑和檔案。
# splitdrive(): 分割檔案路徑名稱為磁碟機和檔案路徑名稱。
# join(): 將路徑和檔案名稱結合為完整路徑。

# 檢查指定的檔案或路徑是否存在。
# 檢查 ospath.py 檔案是否存在，如果檔案存在顯示其完整路徑名稱並計算檔案大小。

import os

filename = os.path.abspath("demo.txt")

if os.path.exists(filename): # 檢查檔案是否存在
    print(f"完整路徑名稱: {filename}")
    print(f"檔案大小: {os.path.getsize(filename)}")
else:
    print(f"檔案不存在!")
    c_file = input("請問是否要為您建立? 請輸入Y/N?")
    try:
        if c_file == "Y":
            cur_path = os.getcwd()
            os.open(f"demo.txt", os.O_RDWR|os.O_CREAT) # 建立一個可讀寫的 demo.txt
        else:
            print("結束程式!")
    except:
        print("請輸入Y/N")

# 完整路徑名稱: C:\...\...\Doc...\Git...\python-training\programing-bible\demo.txt
# 檔案大小: 3
