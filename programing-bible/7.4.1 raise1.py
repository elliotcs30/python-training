# 主動拋出速度過快或太慢例外
# 高速公路設定速限為 70~110，如果速度過快或太慢，就主動拋出例外，提醒用路人注意安全。

def CheckSpeed(speed): # 檢查速度
    if speed < 70:
        raise Exception("速度太慢了!") # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("已經超速了!") # 拋出 Exception 型別例外

for speed in (60, 100, 150):
    try:
        CheckSpeed(speed) #檢查速度
    except Exception as e: # 接收 Exception 的例外
        print(f"現在速度{speed, e}")
    else:
        print(f"目前時速: {speed}")