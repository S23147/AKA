from django.db import models
from patients.models import Patient

class SmartCard(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    numero_carte = models.CharField(max_length=20, unique=True)
    date_activation = models.DateTimeField(auto_now_add=True)
    derniere_utilisation = models.DateTimeField(auto_now=True)
    code_barre_urgence = models.CharField(max_length=50, unique=True, blank=True, null=True)
    expiration_code_barre = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Carte {self.numero_carte} - {self.patient.first_name} {self.patient.last_name}"
