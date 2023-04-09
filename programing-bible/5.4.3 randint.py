# 擲骰子遊戲
# 程式設計讓阿寶按任意鍵再按 Enter 鍵擲骰子，會顯示 1 到 6 之間的整數亂數代表骰子點數，直接按 Enter 鍵會結束遊戲。

import random as r

while True:
    inkey = input("按任意鍵再按[Enter]鍵擲骰子，直接按[Enter]鍵結束:")
    if len(inkey) > 0:
        num = r.randint(1, 6)
        print(f"你擲的骰子點數為: {str(num)}")
    else:
        print("遊戲結束！ ")
        break