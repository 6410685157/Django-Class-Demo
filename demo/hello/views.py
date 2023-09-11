from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, workd!")

def greet(request, name):
    return render(request, 'hello/greet.html', {
        "name": name.title()
    })