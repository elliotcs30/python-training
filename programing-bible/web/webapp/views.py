from django.shortcuts import render
from django.http import HttpResponse
import random

def sayhello(request):
    return HttpResponse("Hello Django!")

def dice(request):
    nums = list(range(1, 7))
    no1 = random.choice(nums) # 1 ~ 6
    nums.remove(no1)          # 移除 no1 已出現過的數字
    no2 = random.choice(nums) # 從移除 no1 的數值陣列中再取出 1 個隨機的數字
    nums.remove(no2)          # 移除 no2 已出現過的數字
    no3 = random.choice(nums) # 從移除 no1、no2 的數值陣列中再取出 1 個隨機的數字
    
    # 使用 locals() 傳遞所有的區域變數
    return render(request, "dice.html", locals())
