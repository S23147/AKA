from django.db import models
from patients.models import Patient
from hopital.models import Laboratoire
from django.conf import settings
from django.apps import apps
from django.contrib.auth import get_user_model

User = get_user_model()

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="consultations")
    medecin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    diagnostic = models.TextField()
    traitement = models.TextField()
    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.SET_NULL, null=True, blank=True)

    motif_consultation = models.TextField(verbose_name="Motif de consultation", blank=True, null=True)
    type_consultation = models.CharField(max_length=100, blank=True, null=True)
    notes_consultation = models.TextField(blank=True, null=True)
    poids = models.FloatField(blank=True, null=True)
    taille = models.FloatField(blank=True, null=True)
    pression_arterielle = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    frequence_cardiaque = models.IntegerField(blank=True, null=True)
    symptomes = models.TextField(blank=True, null=True)
    traitement_recommande = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consultation {self.id} - {self.patient.first_name} {self.patient.last_name}"

class Ordonnance(models.Model):
    consultation = models.OneToOneField(Consultation, on_delete=models.CASCADE, related_name="ordonnance")
    date_prescription = models.DateTimeField(auto_now_add=True)
    instructions = models.TextField(help_text="Instructions d'utilisation")

    def __str__(self):
        return f"Ordonnance pour {self.consultation.patient} - {self.consultation.date.strftime('%d/%m/%Y')}"

class Prescription(models.Model):
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    medicament_id = models.PositiveIntegerField()
    quantite = models.PositiveIntegerField()

    def get_medicament(self):
        Medicament = apps.get_model('pharmacie', 'Medicament')
        return Medicament.objects.get(id=self.medicament_id)

    def __str__(self):
        return f"{self.quantite}x {self.get_medicament().nom}"
