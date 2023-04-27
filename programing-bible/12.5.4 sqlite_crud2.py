# 新增資料
import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線

# 定義資料串列
datas = [[1, 'Elliot', '02-123456789'],
        [2, 'Bonnie', '03-123456789'],]

# 新增資料
for data in datas:
    conn.execute(f"INSERT INTO contact (id, name, tel) VALUES({data[0]}, '{data[1]}', '{data[2]}')")

conn.commit() # 更新
conn.close() # 關閉資料庫連線