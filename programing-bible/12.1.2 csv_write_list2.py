# 將二維串列資料寫入 csv 檔案
import csv

# 建立 csv 二維串列資料
csvtable = [
    ['姓名', '身高', '體重'],
    ['Elliot', 168, 60],
    ['Bonnie', 165, 50],
]

# 開啟輸出的 csv 檔案
with open('test2.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    # 建立 csv 檔寫入物件
    writer = csv.writer(csvfile)
    
    # 寫入二維串列資料
    writer.writerows(csvtable)