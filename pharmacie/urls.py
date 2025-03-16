from django.urls import path
from .views import pharmacie_dashboard, add_medicament, medicament_list, order_list

app_name = 'pharmacie'  # Assurez-vous d'ajouter l'app_name pour le namespace

urlpatterns = [
    path('', pharmacie_dashboard, name='pharmacie_dashboard'),
    path('add/', add_medicament, name='add_medicament'),
    path('list/', medicament_list, name='medicament_list'),
    path('orders/', order_list, name='pharmacie_orders'),
]
