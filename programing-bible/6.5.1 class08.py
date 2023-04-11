# Child 子類別同時以「class Child(Father, Mother)」繼承 Father、Mother 類別，並繼承 say() 方法。

class Father():     # 定義父類別
    def say(self):  # 定義共用方法
        print("明天會更好!")

class Mother():     # 定義父類別
    def say(self):
        print("包容、尊重!")

class Child(Father, Mother): # 定義子類別
    pass

child = Child() # 建立 child 物件
child.say()     # 明天會更好! (優先找 Child 的 say 方法，若找不到再找 Father，再找不到再找 Mother 的 say 方法)