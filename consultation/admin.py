from django.contrib import admin
from .models import Consultation, Ordonnance, Prescription

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'date', 'diagnostic')  # ✁ECorrection ici
    search_fields = ('patient__first_name', 'patient__last_name', 'medecin__username')  # ✁ECorrection ici
    list_filter = ('date', 'medecin')  # ✁ECorrection ici

@admin.register(Ordonnance)
class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('consultation', 'date_prescription')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('ordonnance', 'medicament_display', 'quantite')

    def medicament_display(self, obj):
        return str(obj.get_medicament()) if hasattr(obj, 'get_medicament') else "N/A"
    medicament_display.short_description = "Médicament"
