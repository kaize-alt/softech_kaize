from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def OrdersIndex(request):
    return HttpResponse('<h1>Страница приложения Заказов</h1>')