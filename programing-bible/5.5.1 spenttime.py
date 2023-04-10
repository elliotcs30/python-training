# 計算執行時間
# 許多資訊競賽會使用演算法，除了比程式執行的正確性，也會比程式執行的時間。
# 下列程式會執行迴圈 100 次，並在每次迴圈中暫停 0.001 秒，模擬程式執行總共花費的時間。

import time

start = (time.time()) # 開始執行時間
print(f" 開始時間: {start}")

for i in range(100):
    time.sleep(0.001)

end = (time.time()) # 結束執行時間
print(f" 結束時間: {end}")
print(f" 使用時間: {end - start:6.3f} 秒")