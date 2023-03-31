# 集合的方法

# add()
langs1 = {'Python', 'JavaScript', 'Kotlin'}
langs1.add('C++')
langs1.add('Python')
print(langs1) # {'Python', 'JavaScript', 'Kotlin', 'C++'}

# clear()
langs2 = {'Python', 'JavaScript', 'Kotlin'}
ret = langs2.clear()
print(ret) # None
print(langs2) # set()

# copy()
langs3 = {"Python", "JavaScript", "Kotlin"}
langs_copy = langs3.copy()
langs_copy.add("C++")
print(langs3) # {'Kotlin', 'Python', 'JavaScript'}
print(langs_copy) # {'Kotlin', 'Python', 'JavaScript', 'C++'}

# discard()
# 刪除指定的集合元素，如果指定的元素不存在也不會傳回錯誤
langs4 = {"Python", "JavaScript", "Kotlin"}
langs4.discard("Python")
langs4.discard("C++")
print(langs4) # {'JavaScript', 'Kotlin'}

# remove()
# 刪除指定的集合元素，如果指定的元素不存在將會產生 KeyError
langs5 = {"Python", "JavaScript", "Kotlin"}
langs5.remove("Python") # {'JavaScript', 'Kotlin'}
langs5.remove("C++")  # langs5.remove("C++")  KeyError: 'C++
print(langs5) # {'JavaScript', 'Kotlin'}

# pop()
# 隨機刪除集合 langs 的集合，刪除空集合 langs 再將會產生 KeyError 錯誤
langs6 = {"Python", "JavaScript", "Kotlin"}
item = langs6.pop()
print(item) # Python
print(langs6) # {'JavaScript', 'Kotlin'}
langs6.clear() # KeyError: 'pop from an empty set'

# update()
# A.update(B) 將集合 B 的元素加入集合 A 中
A = {"Python", "JavaScript", "Kotlin"}
B = {"Python", "C"}
A.update(B)
print(A) # {'Python', 'JavaScript', 'Kotlin', 'C'}
print(B) # {'Python', 'C'}