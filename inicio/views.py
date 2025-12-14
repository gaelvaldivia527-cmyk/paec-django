# Importa la función render, que sirve para mostrar archivos HTML
from django.shortcuts import render

# Importa los modelos Planta y Pedido para trabajar con la base de datos
from .models import Planta, Pedido


# =====================================================
#              PÁGINA DE INICIO
# =====================================================
def inicio(request):
    # Muestra la página principal del sistema
    return render(request, "inicio.html")


# =====================================================
#        PÁGINA DE INFORMACIÓN DEL PAEC
# =====================================================
def info_paec(request):
    # Carga la página con información general del proyecto
    return render(request, "info_paec.html")


# =====================================================
#        PÁGINA DE GUÍAS DE SIEMBRA
# =====================================================
def guias_siembra(request):
    # Muestra recomendaciones para plantar árboles
    return render(request, "guias_siembra.html")


# =====================================================
#        PÁGINA DE CALCULADORA
# =====================================================
def calculadora_distancias(request):
    # Muestra la calculadora de distancias entre brotes
    return render(request, "calculadora.html")


# =====================================================
#        PÁGINA DE COMPOSTAS Y SUSTRATOS
# =====================================================
def compostas_sustratos(request):
    # Carga la página sobre compostas
    return render(request, "compostas.html")


# =====================================================
#        PÁGINA DE PROBLEMAS DE LA REGIÓN
# =====================================================
def problemas_region(request):
    # Muestra los problemas ambientales de la región
    return render(request, "problemas_region.html")


# =====================================================
#        PÁGINA DE ÁRBOLES DE LA REGIÓN
# =====================================================
def arboles_region(request):
    # Muestra información de árboles locales
    return render(request, "arboles_region.html")


# =====================================================
#        FUNCIÓN PRINCIPAL PARA PEDIR PLANTAS
# =====================================================
def pedir_plantas(request):

    # Obtiene las plantas según su tipo desde la base de datos
    maderables = Planta.objects.filter(tipo="Maderable")
    sombra = Planta.objects.filter(tipo="Sombra")
    frutales = Planta.objects.filter(tipo="Frutal")

    # Obtiene todas las plantas disponibles
    plantas = Planta.objects.all()

    # Variable para mostrar mensajes de error al usuario
    mensaje = None

    # Verifica si el formulario fue enviado
    if request.method == "POST":

        # Obtiene el nombre ingresado por el usuario
        nombre = request.POST.get("nombre")

        # Obtiene la localidad (puede venir vacía)
        localidad = request.POST.get("localidad", "")

        # Obtiene el ID de la planta seleccionada
        planta_id = request.POST.get("planta")

        # Obtiene la cantidad solicitada y la convierte a número entero
        cantidad = int(request.POST.get("cantidad", 0))

        # Busca la planta seleccionada en la base de datos
        planta = Planta.objects.get(id=planta_id)

        # Valida que la cantidad sea mayor a cero
        if cantidad <= 0:
            mensaje = "❌ La cantidad debe ser mayor a cero."

        # Valida que haya suficientes plantas disponibles
        elif cantidad > planta.cantidad_disponible:
            mensaje = "❌ No hay suficientes plantas disponibles."

        else:
            # Resta la cantidad solicitada del inventario
            planta.cantidad_disponible -= cantidad

            # Guarda el cambio en la base de datos
            planta.save()

            # Guarda el pedido en la base de datos
            Pedido.objects.create(
                nombre_persona=nombre,
                localidad=localidad,
                planta=planta,
                cantidad=cantidad
            )

            # Muestra el ticket con la información del pedido
            return render(request, "ticket.html", {
                "nombre": nombre,
                "localidad": localidad,
                "planta": planta.nombre,
                "cantidad": cantidad,
                "restantes": planta.cantidad_disponible,
            })

    # Si no se envió el formulario o hubo error, vuelve a mostrar la página
    return render(request, "pedir_plantas.html", {
        "maderables": maderables,
        "sombra": sombra,
        "frutales": frutales,
        "plantas": plantas,
        "mensaje": mensaje,
    })
