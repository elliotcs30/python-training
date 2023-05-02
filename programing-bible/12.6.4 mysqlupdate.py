# 更新資料
# update 資料表 set 欄位1 = 值1, 欄位2 = 值2 ... 條件式
import pymysql

# 連結資料庫
conn = pymysql.connect(
    host='localhost', 
    port=3306, user='root', 
    passwd='1234', 
    charset='utf8', 
    db='pythondb')

with conn.cursor() as cursor:
    sql = "update scores set Chinese = 98 where ID = 4"
    cursor.execute(sql)
    conn.commit()
    sql = "select * from scores where ID = 4"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)