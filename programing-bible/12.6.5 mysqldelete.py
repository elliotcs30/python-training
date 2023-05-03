# 刪除資料
# delete from 資料表 where 條件式
import pymysql

# 連結資料庫
conn = pymysql.connect(
    host='localhost', 
    port=3306, user='root', 
    passwd='1234', 
    charset='utf8', 
    db='pythondb')

with conn.cursor() as cursor:
    sql = "delete from scores where ID = 4"
    cursor.execute(sql)
    conn.commit()
    sql = "select * from scores"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)