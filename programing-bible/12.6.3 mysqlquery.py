# 查詢資料
import pymysql

# 連結資料庫
conn = pymysql.connect(
    host='localhost', 
    port=3306, user='root', 
    passwd='1234', 
    charset='utf8', 
    db='pythondb')

with conn.cursor() as cursor:
    sql = "select * from scores"
    cursor.execute(sql) # 執行 SQL 指令
    datas = cursor.fetchall() # 取出所有資料
    print(datas)
    print('-' * 30)
    sql = "select * from scores"
    cursor.execute(sql)
    data = cursor.fetchone() # 取出第一筆資料
    print(data)
    conn.commit() # 提交資料庫
conn.close()