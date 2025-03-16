from django.apps import AppConfig
from django.db.utils import OperationalError

class AccessManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'access_management'

    def ready(self):
        try:
            import access_management.signals  # ✁ESécurisation pour éviter l'erreur
        except ModuleNotFoundError:
            pass  # ✁EIgnorer l'erreur si le fichier signals.py n'existe pas encore
        
