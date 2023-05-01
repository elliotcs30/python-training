# 更新資料
# update 資料表 set  欄位1 = 值1, 欄位2 = 值2, where 條件式

import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線

# 更新資料
conn.execute("UPDATE contact SET name='{}' WHERE id={}".format('Ken', 1))
conn.commit() # 更新
conn.close() # 關閉資料庫連線