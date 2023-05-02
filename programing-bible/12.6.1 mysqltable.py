# 在 pythondb 資料庫中新增 score 資料表，並定義座號(ID)、姓名(Name)、國文(Chinese)、英文(English)、數學(Math)

# pip install pymysql

import pymysql

# 連結資料庫
conn = pymysql.connect(
    host='localhost', 
    port=3306, user='root', 
    passwd='1234', 
    charset='utf8', 
    db='pythondb')

with conn.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS Scores(
        ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Name varchar(20),
        Chinese int(3),
        English int(3),
        Math int(3)
    )
    """
    cursor.execute(sql) # 執行 SQL 指令
    conn.commit() # 提交資料庫
conn.close()