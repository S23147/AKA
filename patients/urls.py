from django.urls import path
from .views import (
    patient_list, add_patient, edit_patient, dashboard, 
    get_patients, custom_login, superadmin_dashboard, 
    ministere_dashboard, services_dashboard, pharmacie_dashboard, add_prescription
)
from django.contrib.auth import views as auth_views

app_name = 'patients'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  
    path('list/', patient_list, name='patient_list'),
    path('add/', add_patient, name='add_patient'),
    path('edit/<int:patient_id>/', edit_patient, name='edit_patient'),
    path('api/', get_patients, name='get_patients'),
    path('login/', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    path('superadmin_dashboard/', superadmin_dashboard, name='superadmin_dashboard'),
    path('ministere_dashboard/', ministere_dashboard, name='ministere_dashboard'),
    path('services_dashboard/', services_dashboard, name='services_dashboard'),
    path('pharmaceutique_dashboard/', pharmacie_dashboard, name='pharmaceutique_dashboard'),
]
