from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importation nécessaire
from django.shortcuts import render
from patients.views import superadmin_dashboard, services_dashboard, ministere_dashboard, custom_login
from pharmacie.views import pharmacie_dashboard

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('hopital/', include('hopital.urls', namespace='hopital')),  # Namespace ajouté
    path('patients/', include('patients.urls', namespace='patients')),  # Namespace ajouté
    path('consultation/', include('consultation.urls', namespace='consultation')),  # Namespace ajouté
    path('pharmacie/', include('pharmacie.urls', namespace='pharmacie')),  # Namespace ajouté
    path('healthcard/', include('healthcard.urls', namespace='healthcard')),  # Namespace ajouté
    path('access_management/', include('access_management.urls', namespace='access_management')),  # Namespace ajouté

    # Routes de connexion et déconnexion
    path('accounts/login/', custom_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # Routes pour l'authentification

    # Déconnexion avec redirection vers la page d'accueil
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Dashboards
    path('ministere/dashboard/', ministere_dashboard, name='ministere_dashboard'),
    path('superadmin_dashboard/', superadmin_dashboard, name='superadmin_dashboard'),
    path('services_dashboard/', services_dashboard, name='services_dashboard'),
    path('pharmacie_dashboard/', pharmacie_dashboard, name='pharmacie_dashboard'),
]
