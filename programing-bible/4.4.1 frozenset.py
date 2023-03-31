# 凍結集合
# 建立凍結集合並執行集合的操作和基本函式
# 但不能執行 add(), clear(), discard(), pop(), remove(), update() 等更新集合的函式

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A & B) # frozenset({3, 4})
print(A | B) # frozenset({1, 2, 3, 4, 5, 6})
print(A - B) # frozenset({1, 2})
print(A ^ B) # frozenset({1, 2, 5, 6})

print(max(A)) # 4
print(sum(A)) # 10