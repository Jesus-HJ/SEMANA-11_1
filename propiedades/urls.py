from django.urls import path
from . import views

# Espacio de nombres para reversibilidad de URLs: {% url 'propiedades:nombre' %}
app_name = 'propiedades'

urlpatterns = [
    # Ruta principal (FBV: home)
    path('', views.home, name='home'),
    # Ruta del catálogo (CBV: PropiedadListView)
    path('propiedades/', views.PropiedadListView.as_view(), name='catalogo'),
]
