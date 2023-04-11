# 取得父類別的私用屬性
# 在子類別中以 super().getEye() 取得父類別的私用屬性「self.__eye」。

class Father():
    def __init__(self, name):
        self.name = name
        self.__eye = "黑色" # 定義私用屬性
    def getEye(self):       # 定義共用方法傳回私用屬性 
        return self.__eye

class Child(Father):        # 定義子類別
    def __init__(self, name, eye):
        super().__init__(name)
        self.eye = eye
        self.fatherEye = super().getEye() # 取得私用屬性

joe = Child("小明", "棕色") # 建立子類別物件 joe
print(f"{joe.name}眼睛是{joe.eye}，他的父親眼睛是{joe.fatherEye}") # 小明眼睛是棕色，他的父親眼睛是黑色