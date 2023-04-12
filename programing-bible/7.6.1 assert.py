# assert 斷言速度不可為負
# 建立 Car 類別並以建構式設定速度，Turbo() 方法可以增加速度 n，
# 若初速 < 0，以 assert 斷言拋出此速度不可為負的例外。

class Car():
    def __init__(self, speed):
        self.speed = speed
    
    def Turbo(self, n): # 增加速度 n
        assert speed >= 0, '速度不可能為負!'
        self.speed += n

for speed in (60, -20):
    bus = Car(speed)
    print("初速 =", bus.speed, end=" ")
    bus.Turbo(50)
    print("加速後，速度 =", bus.speed)

# 停用斷言
# python -O file.py
