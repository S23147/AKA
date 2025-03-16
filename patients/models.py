from django.db import models
from django.utils import timezone
from hopital.models import Hopital
from django.contrib.auth.models import AbstractUser
import random
from django.apps import apps
import datetime
from django.contrib.auth import get_user_model

# Modèle pour les utilisateurs personnalisés
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('medecin', 'Médecin'),
        ('pharmacien', 'Pharmacien'),
        ('patient', 'Patient'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient', verbose_name="Rôle")

    def __str__(self):
        return f"{self.username} ({self.role})"

# Modèle pour les patients
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Autre'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="patient_profile")
    first_name = models.CharField(max_length=100, verbose_name="Prénom", default="Inconnu")
    last_name = models.CharField(max_length=100, verbose_name="Nom", default="Inconnu")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Genre", default="O")
    date_of_birth = models.DateField(verbose_name="Date de naissance", default=timezone.now)
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Numéro de téléphone", default="0000000000")
    email = models.EmailField(unique=True, verbose_name="Email", blank=True, null=True)
    address = models.TextField(verbose_name="Adresse", default="Adresse inconnue")
    emergency_contact = models.CharField(max_length=100, verbose_name="Contact d'urgence", default="Non spécifié")
    blood_type = models.CharField(max_length=5, verbose_name="Groupe sanguin", blank=True, null=True)
    medical_history = models.TextField(verbose_name="Antécédents médicaux", blank=True, null=True)
    insurance_number = models.CharField(max_length=50, verbose_name="Numéro d'assurance", blank=True, null=True)
    chronic_diseases = models.TextField(verbose_name="Maladies chroniques", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    identifiant_cmu = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name="Identifiant CMU")

    hopital = models.ForeignKey(Hopital, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Hôpital assigné")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - CMU: {self.identifiant_cmu if self.identifiant_cmu else 'Non attribué'}"

    def generer_identifiant_cmu(self):
        """ Générer un identifiant unique pour le patient """
        if not self.date_of_birth:
            return None
        date_part = self.date_of_birth.strftime("%Y%m%d") if isinstance(self.date_of_birth, (datetime.date, datetime.datetime)) else None
        numero_unique = random.randint(10000, 99999)
        return f"{date_part}{numero_unique}"

    def save(self, *args, **kwargs):
        """ Sauvegarder les informations du patient, y compris l'identifiant CMU """
        if not self.identifiant_cmu:
            self.identifiant_cmu = self.generer_identifiant_cmu()

        if not self.hopital:
            Hopital = apps.get_model('hopital', 'Hopital')
            self.hopital = Hopital.objects.order_by('?').first()  

        super().save(*args, **kwargs)

# Modèle pour les prescriptions
from pharmacie.models import Medicament

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    dose = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    prescribed_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    date_prescribed = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Prescription for {self.patient.first_name} {self.patient.last_name} - {self.medicament.name}"
