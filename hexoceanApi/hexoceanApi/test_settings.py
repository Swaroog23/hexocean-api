from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'hexocean',
        "USER": 'Admin',
        "HOST": "db",
        "PORT": "5432",
        "PASSWORD": "Admin123"
    }
}