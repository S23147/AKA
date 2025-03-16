from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'email']
    search_fields = ['username', 'email', 'role']
    list_filter = ['role']

admin.site.register(CustomUser, CustomUserAdmin)

# Enregistrer les permissions pour le Ministère de la Santé
class MinisterePermissionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'codename']

admin.site.register(Permission, MinisterePermissionsAdmin)

# Vérifie si le modèle n'est pas déjà enregistré avant de l'ajouter
if not admin.site.is_registered(Group):
    admin.site.register(Group)
