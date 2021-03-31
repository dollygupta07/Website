from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
def indexView(request):
    context = {
    	'events':Event.objects.all()
    }
    return render(request,'event/index.html',context)
