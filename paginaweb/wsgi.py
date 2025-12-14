"""
WSGI config for paginaweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

# 📌 Indicamos a Django qué archivo de settings usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginaweb.settings')

# 🔧 Inicializamos Django
django.setup()

# ==============================
# ⚙️ SOLO PARA RENDER (FREE)
# ==============================
if os.environ.get("RENDER"):

    from django.core.management import call_command

    # 🗄️ Ejecutar migraciones
    try:
        call_command('migrate', interactive=False)
        print("✔ Migraciones aplicadas correctamente")
    except Exception as e:
        print("⚠ Aviso migrate:", e)

    # 🌱 Cargar datos iniciales (PLANTAS)
    try:
        call_command('loaddata', 'plantas', verbosity=0)
        print("✔ Plantas cargadas desde fixture")
    except Exception as e:
        print("⚠ Aviso loaddata:", e)

    # 🎨 Recolectar archivos estáticos (ADMIN CSS)
    try:
        call_command('collectstatic', interactive=False, clear=True)
        print("✔ Static files recolectados")
    except Exception as e:
        print("⚠ Aviso collectstatic:", e)

    # 👤 Crear superusuario automático
    try:
        import createsuperuser_render
        print("✔ Superusuario verificado/creado")
    except Exception as e:
        print("⚠ Aviso superusuario:", e)

# 🚀 Crear la aplicación WSGI (AL FINAL)
application = get_wsgi_application()
