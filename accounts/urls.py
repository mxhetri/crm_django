from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', home),
    path('products/', products),
    path('customer/', customer,)
]