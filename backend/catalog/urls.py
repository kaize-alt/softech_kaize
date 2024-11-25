from django.urls import path

from .views import *

urlpatterns = [
    path('catalog/<slug:catalog_name>/', catalogIndex),
]
