# 類別繼承
# 建立父類別 Animal，包含 name、fly 共用屬性和方法，
# 再建立子類別 Bird 繼承 Animal 類別，並在 Bird 類別中建立另一個共用方法 sing。

class Animal():
    def __init__(self, name):
        self.name = name # 定義共用屬性
    def fly(self):       # 定義共用方法
        print(f"{self.name} 會飛!")

class Bird(Animal): # 定義子類別
    def __init__(self, name):
        self.name = f"粉紅色 {name}" # 覆寫覆類別的建構式
    def sing(self): # 定義子類別的方法
        print(f"{self.name} 會唱歌!")

pigeon = Animal("小鴿子") # 以 Animal 類別，建立一個名叫小鴿子的 pigeon 物件
pigeon.fly() # 小鴿子會飛!

parrot = Bird("小鸚鵡") # 以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
parrot.fly()  # 粉紅色 小鸚鵡 會飛!
parrot.sing() # 粉紅色 小鸚鵡 會唱歌!
