from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def hello_world(request, name):
    return HttpResponse(f"Hello{name}")
'''

def top(request):
    return render(request, 'nagoyameshi/top.html')


'''
def search(request, ):
    return HttpResponse()

def login(request, ):
    return HttpResponse()

def register(request, ):
    return HttpResponse()
'''