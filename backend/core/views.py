from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>', status = 404)