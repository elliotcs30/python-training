# 集合的基本函式

# enumerated(): 傳回連續整數配對的 enumerated 物件
# len(): 元素長度
# max(): 最大值
# min(): 最小值
# sorted(): 傳回排序的新串列，原來的集合不變
# sum(): 總和

langs = {"Pyhton", "JavaScript", "PHP"}
sortlangs = sorted(langs) # 由小到大
sortlangs2 = sorted(langs, reverse=True) # 由大到小
print(sortlangs) # ['JavaScript', 'PHP', 'Pyhton']
print(sortlangs2) # ['Pyhton', 'PHP', 'JavaScript']


langs2 = {"Python", "JavaScript", "PHP"}
enum_langs = enumerate(langs2) # 轉換為 enumerate 物件
print(type(enum_langs)) # <class 'enumerate'>

# 轉成串列
print(list(enum_langs)) # [(0, 'Python'), (1, 'JavaScript'), (2, 'PHP')]
for item in enumerate(langs2):
    print(item)

for i, item in enumerate(langs2):
    print(i, item)