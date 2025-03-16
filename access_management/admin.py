from django.contrib import admin
from django.contrib.auth.models import Permission, Group
from .models import Role, CustomUser

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'email']
    search_fields = ['username', 'email', 'role']
    list_filter = ['role']

# Vérifie si `Permission` n'est pas déjà enregistré avant de l'ajouter
if not admin.site.is_registered(Permission):
    @admin.register(Permission)
    class MinisterePermissionsAdmin(admin.ModelAdmin):
        list_display = ['name', 'codename']

# Vérifie si `Group` n'est pas déjà enregistré avant de l'ajouter
if not admin.site.is_registered(Group):
    admin.site.register(Group)
