# 用 openpyxl 模組儲存 xlsx 檔
import openpyxl

# 建立一個工作簿
workbook = openpyxl.Workbook()

# 取得第一個工作表
sheet = workbook.worksheets[0]

# 以儲存格位置寫入資料
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# 以串列寫入資料
listtitle = ["姓名", "電話"]
sheet.append(listtitle)
listdata=["Elliot", "0912-123123"]
sheet.append(listdata)
# 儲存檔案
workbook.save('test.xlsx')