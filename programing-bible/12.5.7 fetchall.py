import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線

cursor = conn.execute('select * from contact')
rows = cursor.fetchall()  # or fetchone() 顯示資料表中第一筆資料

# 顯示原始資料
print(rows)

# 逐筆資料顯示
for row in rows:
    print(row[0], row[1])

conn.commit()
conn.close()