# 集合
# 使用大括號建立集合
fruits1 = {'apple', 'banana', 'cherry'}
print(fruits1)
print(type(fruits1))

# 重複的元素，多餘的會被捨去
fruits2 = {'apple', 'banana', 'cherry', 'apple'}
print(fruits2)

# 使用不同的型別的元素
fruits3 = {'apple', 'banana', 'cherry', (1, 2), 100}
print(fruits3)

# 集合不可以使用串列、字典

# 使用 set() 函式建立集合
fruits4 = set(['apple', 'banana', 'cherry', 'cherry'])
print(fruits4)

# 集合是參數字串，集合元素將轉換成字元，同時會移除重複的字元
s = set("Good Boy!")
print(s) # {'G', 'o', 'd', 'B', 'y', '!'}
print(type(s)) # <class 'set'>

# 建立集合
s2 = set() # 空集合
print(s2) # <class 'set'>


## 去除重複的資料
# EX: 某間企業使用者的資料有很多都是重複的，必須去除重複的資料
persons = ['林XX', '曾XX', '鄭XX', '林XX', '曾XX', '林XX']
s = set(persons) # 串列轉集合
print(s) # {'鄭XX', '林XX', '曾XX'}
list1 = list(s) # 集合轉串列
print(list1) # ['鄭XX', '曾XX', '林XX']
print(list1[0]) # '鄭XX'