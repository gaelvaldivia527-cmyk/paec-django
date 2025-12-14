# Importa el módulo models de Django
# Sirve para definir modelos que se convertirán en tablas de la base de datos
from django.db import models


# =====================================================
#                MODELO DE PLANTAS
# =====================================================

# Se define el modelo Planta
# Este modelo representa las plantas disponibles en el sistema
class Planta(models.Model):

    # TIPO_CHOICES define las opciones permitidas para el tipo de planta
    # Se usa para que el usuario solo pueda elegir entre estos valores
    TIPO_CHOICES = (
        ("Maderable", "Maderable"),
        ("Sombra", "Sombra"),
        ("Frutal", "Frutal"),
    )

    # Campo nombre de la planta
    # CharField se usa para textos cortos
    # max_length=100 limita el tamaño del texto
    nombre = models.CharField(max_length=100)

    # Campo tipo de planta
    # Usa las opciones definidas en TIPO_CHOICES
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Campo que guarda cuántas plantas hay disponibles
    # IntegerField se usa para números enteros
    # default=0 asigna 0 si no se indica un valor
    cantidad_disponible = models.IntegerField(default=0)

    # Método __str__
    # Define cómo se mostrará el objeto Planta en el admin y otros lugares
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


# =====================================================
#                MODELO DE PEDIDOS
# =====================================================

# Se define el modelo Pedido
# Este modelo representa los pedidos realizados por las personas
class Pedido(models.Model):

    # Nombre de la persona que solicita las plantas
    nombre_persona = models.CharField(max_length=100)

    # Localidad de la persona
    # null=True permite que el campo sea NULL en la base de datos
    # blank=True permite que el campo se deje vacío en formularios
    localidad = models.CharField(max_length=100, null=True, blank=True)

    # Relación con el modelo Planta
    # ForeignKey indica que un pedido está asociado a una planta
    # on_delete=models.CASCADE elimina el pedido si la planta se borra
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

    # Cantidad de plantas solicitadas en el pedido
    cantidad = models.IntegerField()

    # Fecha y hora en que se realiza el pedido
    # auto_now_add=True asigna automáticamente la fecha al crearse el registro
    fecha = models.DateTimeField(auto_now_add=True)

    # Método __str__
    # Define cómo se mostrará el pedido en el panel de administración
    def __str__(self):
        return f"Pedido de {self.nombre_persona} - {self.planta.nombre}"

