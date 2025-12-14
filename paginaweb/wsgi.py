"""
WSGI config for paginaweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# 📌 Indicamos a Django qué archivo de settings usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginaweb.settings')

# 🚀 Crear la aplicación WSGI
application = get_wsgi_application()

# ==============================
# ⚙️ SOLO PARA RENDER (FREE)
# ==============================
if os.environ.get("RENDER"):

    # 🔧 Ejecutar migraciones automáticamente
    try:
        from django.core.management import call_command
        call_command('migrate', interactive=False)
        print("Migraciones aplicadas correctamente")
    except Exception as e:
        print("Aviso al ejecutar migrate:", e)

    # 👤 Crear superusuario automático
    try:
        import createsuperuser_render
    except Exception as e:
        print("Aviso al crear superusuario:", e)
