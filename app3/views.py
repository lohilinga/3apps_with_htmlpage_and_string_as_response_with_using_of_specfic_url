from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def seven(request):
    return render(request,'seven.html')
def eight(request):
    return render(request,'eight.html')
def nine(request):
    return HttpResponse('<h1>Life is like a box of chocolates. You never know what you are going to get.</h1>')