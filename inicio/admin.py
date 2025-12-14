# Importa el módulo admin de Django
# Sirve para gestionar los modelos desde el panel de administración
from django.contrib import admin

# Importa los modelos Planta y Pedido desde models.py
# Estos modelos representan tablas de la base de datos
from .models import Planta, Pedido


# ======================================================
#        CONFIGURACIÓN DEL MODELO PLANTA EN EL ADMIN
# ======================================================

# Registra el modelo Planta en el panel de administración
# y lo asocia con la clase PlantaAdmin
@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):

    # list_display indica qué campos se mostrarán como columnas
    # en la lista de plantas dentro del panel de administración
    list_display = ('nombre', 'tipo', 'cantidad_disponible')

    # list_filter agrega filtros en el lado derecho del admin
    # En este caso permite filtrar plantas por su tipo
    list_filter = ('tipo',)

    # search_fields habilita una barra de búsqueda
    # Permite buscar plantas por el campo nombre
    search_fields = ('nombre',)


# ======================================================
#        CONFIGURACIÓN DEL MODELO PEDIDO EN EL ADMIN
# ======================================================

# Registra el modelo Pedido en el panel de administración
# y lo asocia con la clase PedidoAdmin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):

    # list_display define las columnas visibles en la lista de pedidos
    # Muestra información clave de cada pedido realizado
    list_display = ('nombre_persona', 'localidad', 'planta', 'cantidad', 'fecha')

    # list_filter permite filtrar los pedidos
    # Por planta solicitada y por localidad
    list_filter = ('planta', 'localidad')

    # search_fields habilita la búsqueda de pedidos
    # Permite buscar por nombre de la persona o localidad
    search_fields = ('nombre_persona', 'localidad')
