import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginaweb.settings')
django.setup()

from django.contrib.auth.models import User

USERNAME = "admin"
EMAIL = "admin@paec.com"
PASSWORD = "Admin12345"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print("Superusuario creado en Render")
else:
    print("Superusuario ya existe")
