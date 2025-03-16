from django.contrib import admin
from .models import Medicament, SatisfactionOrdonnance, StockMouvement

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ("nom", "quantite_stock", "date_expiration", "categorie")  # ✁ECorrection ici
    list_filter = ("date_expiration", "categorie")  # ✁ECorrection ici
    search_fields = ("nom", "categorie")

@admin.register(SatisfactionOrdonnance)
class SatisfactionOrdonnanceAdmin(admin.ModelAdmin):
    list_display = ("ordonnance", "pharmacien", "statut")
    list_filter = ("statut",)
    search_fields = ("ordonnance__id", "pharmacien__username")

@admin.register(StockMouvement)
class StockMouvementAdmin(admin.ModelAdmin):
    list_display = ("medicament", "quantite", "date_mouvement", "type_mouvement")
    list_filter = ("type_mouvement",)
    search_fields = ("medicament__nom",)
