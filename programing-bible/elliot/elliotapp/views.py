from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def elliothello(request):
    return HttpResponse("Hi, Elliot! Django!")

def homepage(request, username):
    if username == "Elliot":
        username = "admin"
    return render(request, "index.html", locals())