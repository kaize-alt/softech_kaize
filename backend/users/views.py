from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def UsersIndex(request):
    return HttpResponse('<h1>Страница приложения Пользователя</h1>')