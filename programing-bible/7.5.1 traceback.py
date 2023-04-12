# 紀錄例外引發的資訊
# 高速公路設定速限為 70~110，如果速度過快或太慢，就將主動拋出例外資訊的過程紀錄在 <err.txt> 檔案中。

import traceback

def CheckSpeed(speed): # 檢查速度
    if speed < 70:
        raise Exception("speed slow!") # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("speed fast!") # 拋出 Exception 型別例外

for speed in (60, 100, 150):
    try:
        CheckSpeed(speed) # 檢查速度
    except Exception as e: # 接收 Exception 的例外
        with open("err.txt", "a") as f:
            f.write(traceback.format_exc()) # 寫入例外過程
        print("錯誤資訊寫入完成!")
    else:
        print(f"目前時速: {speed}")