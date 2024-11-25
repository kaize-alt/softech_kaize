from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cartIndex(request):
    return render(request, '<h1>Страница приложения Корзины</h1>')