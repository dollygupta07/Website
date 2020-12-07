from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    context = {}
    return render(request,'event/index.html',context)
