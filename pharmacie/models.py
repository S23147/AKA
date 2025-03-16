from django.db import models
from django.conf import settings
from django.apps import apps

class Medicament(models.Model):
    CATEGORIE_CHOICES = [
        ('PNDS', 'Médicament issu du PNDS'),
        ('COMMUN', 'Médicament général'),
    ]

    nom = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    quantite_stock = models.PositiveIntegerField(default=0)
    date_expiration = models.DateField(null=True, blank=True)
    categorie = models.CharField(max_length=10, choices=CATEGORIE_CHOICES, default='COMMUN')

    def __str__(self):
        return f"{self.nom} ({self.get_categorie_display()})"

class SatisfactionOrdonnance(models.Model):
    """
    Modèle pour suivre la satisfaction des ordonnances par les pharmaciens.
    """
    ordonnance = models.ForeignKey('consultation.Ordonnance', on_delete=models.CASCADE, related_name="satisfactions")  # ✁ECorrection
    pharmacien = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Pharmacien"
    )
    statut = models.CharField(max_length=20, choices=[("En attente", "En attente"), ("Validée", "Validée")], verbose_name="Statut")

    def __str__(self):
        return f"Ordonnance {self.ordonnance.id} - {self.statut}"

class StockMouvement(models.Model):
    """
    Modèle pour enregistrer les mouvements de stock des médicaments.
    """
    TYPE_MOUVEMENT_CHOICES = [
        ("Entrée", "Entrée"),
        ("Sortie", "Sortie")
    ]

    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, verbose_name="Médicament")
    quantite = models.IntegerField(verbose_name="Quantité")
    date_mouvement = models.DateTimeField(auto_now_add=True, verbose_name="Date du mouvement")
    type_mouvement = models.CharField(max_length=50, choices=TYPE_MOUVEMENT_CHOICES, verbose_name="Type de mouvement")

    def __str__(self):
        return f"{self.type_mouvement} - {self.medicament.nom} ({self.quantite})"
