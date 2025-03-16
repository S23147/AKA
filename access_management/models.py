# access_management/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Modèle pour les rôles d'utilisateurs
class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
        ('medecin', 'Médecin'),
        ('patient', 'Patient'),
        ('pharmacien', 'Pharmacien'),
        ('ministere', 'Ministère'),
        ('personnel_admin', 'Personnel Administratif'),
        ('bureau_entree', 'Bureau Entrée'),
        ('services', 'Services'),
    ]
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()


# Modèle utilisateur personnalisé
class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")

    # Ajout des related_name pour éviter le conflit entre 'groups' et 'user_permissions'
    groups = models.ManyToManyField('auth.Group', related_name="access_management_customuser_groups", blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name="access_management_customuser_permissions", blank=True)

    def __str__(self):
        return self.username
