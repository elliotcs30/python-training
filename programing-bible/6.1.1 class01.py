# 建立類別 Animal，並在類別建立 name 屬性和方法

class Animal(): # 定義類別
    name = 'bird' # 定義屬性
    def sing(self): # 定義方法
        print("會唱歌!") # 建立物件

bird = Animal()
print(bird.name)
bird.sing()