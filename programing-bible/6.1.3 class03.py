# 建立物件 bird，預設屬性 name = "鸚鵡"、age = 1

class Animal(): # 定義類別
    def __init__(self, name, age):
        self.name = name # 定義屬性
        self.age = age
    def sing(self): # 定義方法
        print(f"{self.name} {str(self.age)} 歲，會唱歌!")
    def grow(self, year): # 定義方法
        self.age += year

bird = Animal("鸚鵡", 1) # 以 Animal 類別，建立一個名叫鸚鵡、 1 歲大的 bird 物件
bird.grow(1) # 長大 1 歲
bird.sing() # 鸚鵡 2 歲，會唱歌!