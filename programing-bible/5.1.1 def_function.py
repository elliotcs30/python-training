# 自訂函式

# 攝氏溫度轉華氏溫度
# 攝氏轉華氏公式: 華氏 = 攝氏 * 1.8+32，設計輸入攝氏溫度，就會轉華氏溫度

def c_to_f(c): # 攝氏轉華氏
    f = c * 1.8 + 32
    return f

input_c = float(input("請輸入攝氏溫度: "))
print(f'華氏溫度為: {c_to_f(input_c):5.1f} 度') 

# 參數預測值
def GetArea(width, height=12): # 預設值要置於參數串列最後，否則會噴錯
    return width * height

ret1 = GetArea(6) # 6 * 12
ret1 = GetArea(6, 10) # 6 * 10

# global 定義全域變數
def scope():
    global var1
    var1 = 1
    var2 = 2
    print(var1, var2) # 1 2

var1 = 10
var2 = 20
scope()
print(var1, var2) # 1 20