from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('take-number/', handle_number, name='take-number'),
    path('number/<int:number>/', show_number_info, name='show-number-info'),
]
