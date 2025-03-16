from django.urls import path
from .views import consultation_dashboard, add_consultation, consultation_history, creer_ordonnance, edit_consultation

# Ajouter l'attribut app_name pour le namespace
app_name = 'consultation'

urlpatterns = [
    path('dashboard/', consultation_dashboard, name='consultation_dashboard'),
    path('add/<int:patient_id>/', add_consultation, name='add_consultation'),
    path('history/<int:patient_id>/', consultation_history, name='consultation_history'),
    path('ordonnance/<int:consultation_id>/', creer_ordonnance, name='creer_ordonnance'),
    path('edit/<int:consultation_id>/', edit_consultation, name='edit_consultation'),
]
