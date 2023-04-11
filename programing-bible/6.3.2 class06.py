# 建立類別 Bird 繼承類別 Animal，子類別 Bird 再以 super() 方法覆寫 __init__() 和 fly 方法。

class Animal(): # 定義父類別
    def __init__(self, name):
        self.name = name # 定義共用屬性
    def fly(self):       # 定義共用方法
        print(f"{self.name}會飛!")

class Bird(Animal): # 定義子類別
    def __init__(self, name, age):
        super().__init__(name) # 執行父類別的 __init__() 方法
        self.age = age # 定義子類別共用屬性
    def fly(self):     # 定義子類別共用方法
        print(str(self.age), end=" 歲")
        super().fly()  # 執行父類別的 fly 方法

pigeon = Animal("小鴿子") # 以 Animal 類別，建立一個名叫小鴿子的 pigeon 物件
pigeon.fly() # 小鴿子會飛!

parrot = Bird("小鸚鵡", 2) # 以 Bird 類別，建立一個名叫小鸚鵡、2歲大的 parrot 物件
parrot.fly() # 2 歲小鸚鵡會飛!