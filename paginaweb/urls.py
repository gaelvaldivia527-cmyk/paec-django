from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),
    path('info-paec/', views.info_paec, name='info_paec'),
    path('guias-siembra/', views.guias_siembra, name='guias_siembra'),
    path('calculadora/', views.calculadora_distancias, name='calculadora'),
    path('pedir-plantas/', views.pedir_plantas, name='pedir_plantas'),
    path('compostas/', views.compostas_sustratos, name='compostas'),
    path('problemas-region/', views.problemas_region, name='problemas'),
    path('arboles-region/', views.arboles_region, name='arboles'),
]
