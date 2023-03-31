# items 顯示世大運獎牌數

# 預期結果:
# 得到的 金牌 數目為 26 面
# 得到的 銀牌 數目為 34 面
# 得到的 銅牌 數目為 30 面

dict1 = { '金牌': 26, '銀牌': 34, '銅牌': 30}

item = list(dict1.items())

for name, num in item:
    print(f'得到的 {name} 數目為 {num} 面')