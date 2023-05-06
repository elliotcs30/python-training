from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def elliothello(request):
    return HttpResponse("Hi, Elliot! Django!")

def sayhello(request, username):
    return HttpResponse(f"Hello, {username}!")

def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def homepage(request, username):
    if username == "Elliot":
        username = "admin"
    return render(request, "index.html", locals())