from django.urls import path
from event import views

app_name = 'event'
urlpatterns = [
    path('',views.indexView, name='index')
]