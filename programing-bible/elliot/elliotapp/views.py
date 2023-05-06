from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def elliothello(request):
    return HttpResponse("Hi, Elliot! Django!")

def sayhello(request, username):
    return HttpResponse(f"Hello, {username}!")