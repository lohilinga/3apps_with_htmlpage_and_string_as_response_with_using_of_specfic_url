from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def four(request):
    return render(request,'four.html')
def five (request):
    return render (request,'five.html')
def six(request):
    return HttpResponse('this my one way')