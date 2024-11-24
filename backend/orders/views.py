from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def OrdersIndex(request, orders_page):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Страница приложения Корзины</h1><p>{orders_page}</p>')