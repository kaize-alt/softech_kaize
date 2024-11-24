from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def CatalogIndex(request, catalog_name ):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Страница приложения Каталога</h1><p>{catalog_name}</p>')