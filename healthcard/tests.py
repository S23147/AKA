from django.urls import path
from .views import read_healthcard

urlpatterns = [
    path('read_card/', read_healthcard, name='read_healthcard'),
]
