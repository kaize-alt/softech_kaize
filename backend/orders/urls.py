from django.urls import path

from .views import *

urlpatterns = [
    path('orders/<slug:orders_page>/', OrdersIndex),
]
