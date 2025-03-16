from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('medecin', 'Médecin'),
        ('pharmacien', 'Pharmacien'),
        ('patient', 'Patient'),
        ('superadmin', 'Super Admin'),
        ('ministere', 'Ministère'),
        ('services', 'Services'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient', verbose_name="Rôle")
    groups = models.ManyToManyField(Group, related_name="users_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="users_permissions", blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


@receiver(post_migrate)
def creer_roles_utilisateurs(sender, **kwargs):
    """
    Crée les groupes d'utilisateurs et leurs permissions après migration.
    """
    if sender.name != "users":  # ✅ Évite d'exécuter cette fonction pour chaque app
        return

    # ✅ Crée les groupes
    groupes = ['Médecins', 'Pharmaciens', 'Patients', 'Administrateurs', 'Ministres de la Santé']
    for groupe in groupes:
        Group.objects.get_or_create(name=groupe)

    # ✅ Détermine un content_type correct
    content_type, _ = ContentType.objects.get_or_create(app_label="users", model="customuser")

    # ✅ Crée les permissions avec un content_type valide
    permissions = [
        ('view_patient', 'Peut voir les patients'),
        ('add_patient', 'Peut ajouter des patients'),
        ('edit_patient', 'Peut modifier des patients'),
        ('delete_patient', 'Peut supprimer des patients'),
        ('view_consultation', 'Peut voir les consultations'),
        ('add_consultation', 'Peut ajouter des consultations'),
        ('manage_stock', 'Peut gérer les stocks'),
    ]

    for codename, name in permissions:
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)
