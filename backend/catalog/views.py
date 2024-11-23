from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def CatalogIndex(request):
    return HttpResponse('<h1>Страница приложения Каталога</h1>')