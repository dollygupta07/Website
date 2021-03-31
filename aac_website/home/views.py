from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    context = {}
    return render(request,'home/index.html',context)

# Create your views here.



