from django.db import models
from hopital.models import Hopital
from django.utils import timezone

class StockMedicamentsEquipements(models.Model):
    stock_id = models.AutoField(primary_key=True)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name="stocks")
    nom_produit = models.CharField(max_length=200)
    quantite = models.IntegerField()
    date_entree = models.DateField(default=timezone.now)
    date_expiration = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom_produit} - {self.hopital.nom_hopital}"
