from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

now = datetime.now().date()


def helloView(request):
    return HttpResponse("<h1>Hello! It's my project</h1>")

def dateView(request):
    return HttpResponse(f'<h1>{datetime.now().date()}</h1>')

def goodbyeView(request):
    return HttpResponse('<h1>Goodbye user!</h1>')