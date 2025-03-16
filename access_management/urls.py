# accès_management/urls.py
from django.urls import path
from .views import (
    redirect_user, admin_dashboard, superadmin_dashboard, medecin_dashboard,
    patient_dashboard, pharmacien_dashboard, ministere_dashboard,
    personnel_admin_dashboard, bureau_entree_dashboard, services_dashboard
)

# Définition du namespace pour l'application 'acces_management'
app_name = 'access_management'

urlpatterns = [
    path('redirect/', redirect_user, name='redirect_user'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('superadmin_dashboard/', superadmin_dashboard, name='superadmin_dashboard'),
    path('medecin_dashboard/', medecin_dashboard, name='medecin_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('pharmacien_dashboard/', pharmacien_dashboard, name='pharmacien_dashboard'),
    path('ministere_dashboard/', ministere_dashboard, name='ministere_dashboard'),
    path('personnel_admin_dashboard/', personnel_admin_dashboard, name='personnel_admin_dashboard'),
    path('bureau_entree_dashboard/', bureau_entree_dashboard, name='bureau_entree_dashboard'),
    path('services_dashboard/', services_dashboard, name='services_dashboard'),
]
