# 計算執行時間
# 許多資訊競賽會使用演算法，除了比程式執行的正確性，也會比程式執行的時間。
# 下列程式會執行迴圈 100 次，並在每次迴圈中暫停 0.001 秒，模擬程式執行總共花費的時間。

import time

start = (time.time()) # 開始執行時間
print(" 開始時間:{}".format(start))

for i in range(100):
    time.sleep(0.001)
end = (time.time()) # 結束執行時間
print(" 結束時間:{}".format(end))
print(" 使用時間:%7.3f 秒" %(end - start))
