
from django.http import HttpResponse
from django.shortcuts import render

def index3(request):
    return render(request,'index.html')

def index2(request):
    return HttpResponse("Hallo Dunia")

def about(request):
    return HttpResponse("about nih")