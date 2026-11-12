from django.test import TestCase
from django.urls import reverse
from propiedades.models import Producto

class InmoAndesModelsAndViewsTestCase(TestCase):
    """
    Suite de pruebas para validar el modelo Producto,
    la CBV PropiedadListView, filtros ORM y la FBV home.
    """

    def setUp(self):
        """Poblar datos de prueba controlados para los tests"""
        self.p1 = Producto.objects.create(
            titulo='Casa San Carlos',
            tipo_inmueble='casa',
            operacion='venta',
            distrito='Huancayo',
            precio=600000.00,
            descripcion='Hermosa casa en San Carlos',
            area_m2=200.00,
            dormitorios=4,
            banos=3,
            destacado=True
        )
        self.p2 = Producto.objects.create(
            titulo='Departamento El Tambo',
            tipo_inmueble='departamento',
            operacion='alquiler',
            distrito='El Tambo',
            precio=1500.00,
            descripcion='Moderno flat cerca a parque',
            area_m2=85.00,
            dormitorios=2,
            banos=1,
            destacado=False
        )
        self.p3 = Producto.objects.create(
            titulo='Terreno Chilca',
            tipo_inmueble='terreno',
            operacion='venta',
            distrito='Chilca',
            precio=120000.00,
            descripcion='Lote con servicios',
            area_m2=150.00,
            destacado=False
        )

    def test_modelo_str(self):
        """Verifica la representación en cadena del modelo Producto"""
        esperado = "Casa San Carlos | Venta en Huancayo - S/ 600000.0"
        self.assertIn("Casa San Carlos", str(self.p1))
        self.assertIn("Venta", str(self.p1))

    def test_home_fbv_queryset(self):
        """Verifica que home obtenga los inmuebles destacados del ORM"""
        response = self.client.get(reverse('propiedades:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Casa San Carlos')

    def test_catalogo_cbv_todos(self):
        """Verifica que el catálogo liste todos los productos sin filtros"""
        response = self.client.get(reverse('propiedades:catalogo'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 3)

    def test_catalogo_filtro_tipo(self):
        """Verifica el filtro GET ?tipo=casa"""
        response = self.client.get(reverse('propiedades:catalogo') + '?tipo=casa')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertContains(response, 'Casa San Carlos')
        self.assertNotContains(response, 'Departamento El Tambo')

    def test_catalogo_filtro_distrito_y_operacion(self):
        """Verifica filtros combinados por distrito y operacion"""
        url = reverse('propiedades:catalogo') + '?distrito=El+Tambo&operacion=alquiler'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertContains(response, 'Departamento El Tambo')

    def test_catalogo_sin_resultados(self):
        """Verifica que un filtro inexistente active el estado vacío"""
        url = reverse('propiedades:catalogo') + '?tipo=local'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 0)
        self.assertContains(response, 'No encontramos propiedades con esos criterios')
