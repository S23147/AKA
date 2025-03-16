from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import Patient

@receiver(post_save, sender=Patient)
def create_dossier_medical(sender, instance, created, **kwargs):
    if created:
        DossierMedical = apps.get_model('patients', 'DossierMedical')
        DossierMedical.objects.create(patient=instance)

@receiver(post_save, sender=Patient)
def save_dossier_medical(sender, instance, **kwargs):
    if hasattr(instance, 'dossier_medical'):
        instance.dossier_medical.save()
