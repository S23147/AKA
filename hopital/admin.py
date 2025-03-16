from django.contrib import admin
from .models import Hopital

class HopitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_hopital', 'categorie', 'adresse_hopital', 'telephone')  # ✁EChamps vérifiés
    list_filter = ('categorie',)
    search_fields = ('nom_hopital', 'adresse_hopital')

admin.site.register(Hopital, HopitalAdmin)
