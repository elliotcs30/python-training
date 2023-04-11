# 建立 Animal 類別，並建立 __init__() 建構式和 sing 方法

class Animal(): # 定義類別
    def __init__(self, name):
        self.name = name # 定義屬性
    def sing(self): # 定義方法
        print(f"{self.name}，很會唱歌!")

bird = Animal("鸚鵡") # 以 Animal 類別，建立一個名叫鸚鵡的 bird 物件
print(bird.name) # 鸚鵡
bird.sing() # 鸚鵡很會唱歌