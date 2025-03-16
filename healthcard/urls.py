from django.urls import path
from . import views

# Définition du namespace pour l'application 'healthcard'
app_name = 'healthcard'

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),  # URL pour ajouter un patient
    path('generate_smartcard/<int:patient_id>/', views.generate_smartcard, name='generate_smartcard'),  # Générer la carte pour un patient
]
