from django.urls import path
from . import views

app_name = 'hopital'  # Définir app_name ici

urlpatterns = [
    path('list/', views.hopital_list, name='hopital_list'),
    path('add/', views.add_hospital, name='add_hopital'),
    path('add_service/', views.add_service, name='add_service'),
    path('add_laboratoire/', views.add_laboratoire, name='add_laboratoire'),
    path('assign_patient/<int:patient_id>/<int:hopital_id>/', views.assign_patient_to_hopital, name='assign_patient_to_hopital'),
]
