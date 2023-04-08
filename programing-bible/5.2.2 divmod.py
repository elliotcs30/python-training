# 學生均分蘋果
# 設計程式輸入學生人數及蘋果總數，將蘋果平均分給學生，每個學生分到的蘋果數量必須相同，計算每個學生分到的蘋果數及剩餘的蘋果數。

student_num = int(input("請輸入學生人數："))
apple_num = int(input("請輸入蘋果總數："))

student_get_apple_num = divmod(apple_num, student_num)
print(f"每個學生可以分得蘋果 {student_get_apple_num[0]} 個")
print(f"蘋果剩餘 {student_get_apple_num[1]} 個")
