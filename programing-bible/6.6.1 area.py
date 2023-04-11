# 計算面積
# 定義 Rectangle、Triangle 兩個類別，父類別 Rectangle 定義共用屬性 width、height 和 area() 方法計算矩形面積。
# Triangle 子類別繼承 Rectangle 類別並增加一個計算三角形面積的方法 area2()。

class Rectangle(): # 定義父類別
    def __init__(self, width, height):
        self.width = width      # 定義共用屬性
        self.height = height    # 定義共用屬性
    def area(self):             # 定義共用方法
        return self.width * self.height

class Triangle(Rectangle):  # 定義子類別
    def area2(self):        # 定義子類別的共用方法
        return (self.width * self.height) / 2

triangle = Triangle(5, 6) # 建立 triangle 物件
print(f"矩形面積 = {triangle.area()}")     # 30
print(f"三角形面積 = {triangle.area2()}")  # 15  