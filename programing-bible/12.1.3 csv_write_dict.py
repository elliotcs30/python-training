# 將字典資料寫入 csv 檔案

import csv
with open('test.csv', 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['name', 'height', 'weight']
    
    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'name': 'Elliot', 'height': 168, 'weight': 60})
    writer.writerow({'name': 'Bonnie', 'height': 156, 'weight': 50})