from django.db import models
from django.contrib.auth.models import User

class Hopital(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    directeur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="hopitaux_diriges")

class Service(models.Model):
    nom = models.CharField(max_length=255)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name="services")

class Laboratoire(models.Model):
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name="laboratoires")
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="labos_gérés")
