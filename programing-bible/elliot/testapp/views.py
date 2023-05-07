from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.
def sayhello(request, username):
    return HttpResponse(f"Hello, {username}!")

def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def hello4(request, username):
    now = datetime.now()
    return render(request, "hello4.html", locals())

def dice(request):
    nums = list(range(1, 7))
    no1 = random.choice(nums) # 1 ~ 6
    nums.remove(no1)          # 移除 no1 已出現過的數字
    no2 = random.choice(nums) # 從移除 no1 的數值陣列中再取出 1 個隨機的數字
    nums.remove(no2)          # 移除 no2 已出現過的數字
    no3 = random.choice(nums) # 從移除 no1、no2 的數值陣列中再取出 1 個隨機的數字
    
    # 使用 locals() 傳遞所有的區域變數
    return render(request, "dice.html", locals())

# 顯示員工資料
def show(request):
    person1 = { "name" : "Elliot", "phone" : "088-1234567", "age" : 18 }
    person2 = { "name" : "Bonnie", "phone" : "099-1234567", "age" : 22 }
    person3 = { "name" : "Gina", "phone" : "081-1234567", "age" : 22}
    persons = [ person1, person2, person3 ]
    return render(request, "show.html", locals())
