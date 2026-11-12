from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

def home(request):
    """
    Vista Basada en Funciones (FBV) para la página de inicio de InmoAndes.
    Demuestra la consulta al ORM mediante filter() sobre el modelo Producto.
    """
    # Consulta ORM: inmuebles con bandera destacado=True (máximo 3)
    destacados = Producto.objects.filter(destacado=True)[:3]
    if not destacados.exists():
        destacados = Producto.objects.all()[:3]

    context = {
        'titulo_pagina': 'Inicio',
        'portal_nombre': 'InmoAndes',
        'eslogan': 'Encuentra el espacio donde comienza tu próxima historia',
        'distritos': ['Huancayo', 'El Tambo', 'Chilca'],
        'tipos': [
            {'nombre': 'Casas', 'slug': 'casa', 'icono': 'bi-house-door', 'conteo': 'Disponibles'},
            {'nombre': 'Departamentos', 'slug': 'departamento', 'icono': 'bi-building', 'conteo': 'Modernos'},
            {'nombre': 'Terrenos', 'slug': 'terreno', 'icono': 'bi-layers', 'conteo': 'Urb. y Campestres'},
            {'nombre': 'Locales', 'slug': 'local', 'icono': 'bi-shop', 'conteo': 'Comerciales'},
        ],
        'propiedades_destacadas': destacados,
    }
    return render(request, 'propiedades/home.html', context)


class PropiedadListView(ListView):
    """
    Vista Basada en Clases (CBV) requerida por la Guía Práctica de la Semana 11.
    Demuestra herencia de ListView, especificación de model, template_name,
    context_object_name, personalización de get_queryset() con lazy evaluation
    y enriquecimiento de contexto mediante get_context_data().
    """
    model = Producto
    template_name = 'propiedades/catalogo.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        """
        Aplica filtros dinámicos mediante parámetros GET del formulario:
        - tipo: casa, departamento, terreno, local
        - distrito: Huancayo, El Tambo, Chilca, etc.
        - operacion: venta, alquiler
        """
        queryset = Producto.objects.all()

        tipo = self.request.GET.get('tipo', '').strip()
        distrito = self.request.GET.get('distrito', '').strip()
        operacion = self.request.GET.get('operacion', '').strip()

        if tipo:
            queryset = queryset.filter(tipo_inmueble__iexact=tipo)
        if distrito:
            queryset = queryset.filter(distrito__iexact=distrito)
        if operacion:
            queryset = queryset.filter(operacion__iexact=operacion)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Pasa variables adicionales al contexto de la plantilla del catálogo.
        """
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Catálogo de Propiedades'
        context['portal_nombre'] = 'InmoAndes'
        context['total_resultados'] = self.get_queryset().count()
        return context
