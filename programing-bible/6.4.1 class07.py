# 定義 Bird 類別繼承 Animal 類別，再定義另一個 Plane 類別，
# 這 3 類別都擁有 fly 方法，此外也建立了一個 fly 函式。

class Animal():     # 定義父類別
    def fly(self):  # 定義共用方法
        print("時速 20 公里!")

class Bird(Animal):       # 定義子類別
    def fly(self, speed): # 定義共用方法
        print(f"時速 {str(speed)} 公里!")

class Plane():     # 定義類別
    def fly(self): # 定義共用方法
        print(f"時速 1000 公里!")

def fly(speed):    # 定義函式
    print(f"時速 {str(speed)} 英哩!")

animal = Animal() # 以 Animal 類別建立 animal 物件
animal.fly() # 時速 20 公里!

bird = Bird() # 以 Bird 類別建立 bird 物件
bird.fly(60) # 時速 60 公里!

plane = Plane() # 以 Plane 類別建立 plane 物件
plane.fly() # 時速 1000 公里!

fly(5) # 時速 5 英哩!