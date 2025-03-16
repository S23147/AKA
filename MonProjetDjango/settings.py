import os
from pathlib import Path
from dotenv import load_dotenv

# 🚀 Chargement des variables d'environnement depuis .env
load_dotenv()

# 📂 Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 Clé secrète Django (à sécuriser via .env)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# 🚨 Mode Debug (Désactive en production)
DEBUG = True

# 🌍 Hôtes autorisés
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '100.116.111.159']

# 🏗️ Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    # 📺 Applications du projet
    'patients',
    'healthcard',
    'hopital',
    'consultation',
    'stock',
    'pharmacie',
    'users',
    'access_management',

    # 🖌 Extensions et Widgets
    'widget_tweaks',
]

# 🔧 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Assurez-vous qu'il est présent
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Assurez-vous qu'il est présent
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌍 Configuration des URLs
ROOT_URLCONF = 'MonProjetDjango.urls'

# 📂 Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ✁ Emplacement correct des templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🛢️ Base de Données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔒 Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Paramètres de Langue et Fuseau Horaire
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📂 Configuration des fichiers statiques et médias
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Assurez-vous que Django charge bien les fichiers statiques
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Configuration de l'authentification Django
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"  # Assurez-vous que la redirection après la connexion est correcte
LOGOUT_REDIRECT_URL = "/"

# 📌 Modèle utilisateur personnalisé
AUTH_USER_MODEL = "access_management.CustomUser"

# 🛠 Paramètre pour éviter l'erreur des migrations Django
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔒 Configuration des sessions
# Désactiver l'expiration automatique de la session et forcer la gestion manuelle
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Utilisation de la base de données pour stocker les sessions
SESSION_COOKIE_AGE = 3600  # La session expire après 1 heure (en secondes)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # La session expire à la fermeture du navigateur
SESSION_COOKIE_SECURE = False  # En production, mettez cette valeur à True si vous utilisez HTTPS
