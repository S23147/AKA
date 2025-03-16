from django.db import models
from django.conf import settings

class Hopital(models.Model):
    """Modèle représentant un hôpital"""
    nom_hopital = models.CharField(max_length=255)  # Nom de l'hôpital
    adresse_hopital = models.TextField()  # Adresse de l'hôpital
    categorie = models.CharField(max_length=255)  # Catégorie de l'hôpital (public, privé, etc.)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    directeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="hopitaux_diriges")
    capacity = models.IntegerField(null=True, blank=True)  # Capacité de l'hôpital (ajouté comme exemple)

    def __str__(self):
        return self.nom_hopital
class Service(models.Model):
    """Modèle représentant un service dans un hôpital"""
    SERVICE_CHOICES = [
        ('dentaire', 'Cabinet Dentaire'),
        ('gynecologie', 'Gynécologie'),
        ('dermatologie', 'Dermatologie'),
        ('soins_intensifs', 'Soins Intensifs'),
        ('pediatrie', 'Pédiatrie'),
        ('autre', 'Autre')
    ]
    nom = models.CharField(max_length=255, choices=SERVICE_CHOICES)  # Liste des services comme cabinet dentaire, etc.
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name="services")
    description = models.TextField()
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  # Responsable du service

    def __str__(self):
        return f"Service {self.nom} de {self.hopital.nom_hopital}"


class Laboratoire(models.Model):
    """Modèle représentant un laboratoire dans un hôpital"""
    nom = models.CharField(max_length=100, verbose_name="Nom du laboratoire")  # Nom du laboratoire
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name="laboratoires")
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  # Responsable (Médecin ou autre)

    def __str__(self):
        return f"Labo {self.nom} de {self.hopital.nom_hopital}"


class AnalyseMedicale(models.Model):
    """Modèle représentant un enregistrement d'analyse médicale pour un patient"""
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name="analyses")
    type_analyse = models.CharField(max_length=255)  # Type de l'analyse (ex: Sang, Urine, etc.)
    resultat = models.TextField(blank=True, null=True)  # Résultat de l'analyse
    date_analyse = models.DateTimeField(auto_now_add=True)  # Date de l'analyse

    def __str__(self):
        if self.patient:
            return f"{self.type_analyse} - {self.patient.first_name} {self.patient.last_name}"
        return str(self.type_analyse)
