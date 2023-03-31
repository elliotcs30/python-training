# setdefault 功能的使用方式、功能及傳回值與 get 雷同
# get 功能不會改變字典的內容； setdefault 功能可能改變字典的內容

dict1 = { 'banana': 20, 'apple': 50, 'orange': 30 }
n = dict1.setdefault('apple', 100) # dict1 未改變
n = dict1.setdefault('pieapple', 100) # {'banana': 20, 'apple': 50, 'orange': 30, 'pieapple': 100}