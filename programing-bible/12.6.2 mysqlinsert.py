# 新增資料
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
    insert into scores (Name, Chinese, English, Math) values
    ('AAA', 95, 92, 80),
    ('BBB', 82, 83, 61),
    ('CCC', 74, 53, 71),
    ('DDD', 86, 87, 89),
    ('EEE', 89, 73, 95)
    """
    cursor.execute(sql) # 執行 SQL 指令
    conn.commit() # 提交資料庫
conn.close()