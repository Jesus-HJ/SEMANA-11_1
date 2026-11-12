from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from propiedades.models import Producto

class Command(BaseCommand):
    help = 'Puebla la base de datos SQLite con 12 inmuebles de demostración para InmoAndes (Huancayo)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando poblado de inmuebles en InmoAndes...'))

        hoy = date.today()

        inmuebles_data = [
            # =================================================================
            # 4 CASAS
            # =================================================================
            {
                'titulo': 'Residencia Contemporánea en San Carlos',
                'tipo_inmueble': 'casa',
                'operacion': 'venta',
                'distrito': 'Huancayo',
                'precio': 680000.00,
                'descripcion': 'Exclusiva residencia de diseño arquitectónico vanguardista en la mejor zona de San Carlos. Cuenta con amplios ventanales, acabados de cedro, jardín interior, sala de estar y cochera para dos camionetas.',
                'area_m2': 240.00,
                'dormitorios': 4,
                'banos': 3,
                'imagen_url': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=2),
                'destacado': True,
            },
            {
                'titulo': 'Casa Quinta Familiar en Urb. La Florida',
                'tipo_inmueble': 'casa',
                'operacion': 'venta',
                'distrito': 'El Tambo',
                'precio': 520000.00,
                'descripcion': 'Hermosa casa familiar con amplio patio, chimenea funcional, cocina con isla y reposteros de cuarzo. Zona residencial tranquila, segura y cercana a colegios de prestigio.',
                'area_m2': 195.00,
                'dormitorios': 4,
                'banos': 3,
                'imagen_url': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=5),
                'destacado': True,
            },
            {
                'titulo': 'Chalet de Estreno con Cochera y Azotea',
                'tipo_inmueble': 'casa',
                'operacion': 'alquiler',
                'distrito': 'Huancayo',
                'precio': 2800.00,
                'descripcion': 'Chalet moderno de dos niveles con excelente iluminación solar todo el año. Cuenta con sala-comedor espaciosa, estudio de trabajo independiente, área de parrillas en la terraza y sistema de videovigilancia.',
                'area_m2': 160.00,
                'dormitorios': 3,
                'banos': 2,
                'imagen_url': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=9),
                'destacado': False,
            },
            {
                'titulo': 'Casa Amplia de 2 Pisos con Huerto Urbano',
                'tipo_inmueble': 'casa',
                'operacion': 'venta',
                'distrito': 'Chilca',
                'precio': 340000.00,
                'descripcion': 'Propiedad espaciosa con potencial de ampliación. Incluye huerto posterior, depósito, cisterna subterránea y acceso inmediato a transporte público y áreas comerciales de Chilca.',
                'area_m2': 180.00,
                'dormitorios': 5,
                'banos': 2,
                'imagen_url': 'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=14),
                'destacado': False,
            },

            # =================================================================
            # 4 DEPARTAMENTOS
            # =================================================================
            {
                'titulo': 'Penthouse de Lujo con Terraza Panorámica',
                'tipo_inmueble': 'departamento',
                'operacion': 'venta',
                'distrito': 'El Tambo',
                'precio': 410000.00,
                'descripcion': 'Impresionante penthouse en piso 8 con vista de 360 grados al Valle del Mantaro. Ascensor directo, terraza con zona BBQ privada, dormitorio principal con jacuzzi y walk-in closet.',
                'area_m2': 135.00,
                'dormitorios': 3,
                'banos': 2,
                'imagen_url': 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=1),
                'destacado': True,
            },
            {
                'titulo': 'Departamento Flat cerca a Open Plaza Huancayo',
                'tipo_inmueble': 'departamento',
                'operacion': 'alquiler',
                'distrito': 'Huancayo',
                'precio': 1600.00,
                'descripcion': 'Flat moderno de estreno en piso 4 con ascensor. Sala iluminada con balcón, cocina americana equipada con gas natural y lavandería ventilada. Vigilancia las 24 horas.',
                'area_m2': 85.00,
                'dormitorios': 2,
                'banos': 2,
                'imagen_url': 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=4),
                'destacado': False,
            },
            {
                'titulo': 'Dúplex Residencial Estratégico cerca a la UNCP',
                'tipo_inmueble': 'departamento',
                'operacion': 'alquiler',
                'distrito': 'El Tambo',
                'precio': 1400.00,
                'descripcion': 'Cómodo dúplex ideal para profesionales, catedráticos o estudiantes universitarios. Ambientes independientes, excelente aislación acústica y cercanía inmediata a la ciudad universitaria.',
                'area_m2': 90.00,
                'dormitorios': 3,
                'banos': 2,
                'imagen_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=7),
                'destacado': False,
            },
            {
                'titulo': 'Departamento Familiar con Excelente Iluminación',
                'tipo_inmueble': 'departamento',
                'operacion': 'venta',
                'distrito': 'Chilca',
                'precio': 215000.00,
                'descripcion': 'Departamento económico y funcional en edificio de 4 pisos. Muy buena distribución interior, gastos comunes mínimos y acceso a colegios y mercados locales.',
                'area_m2': 82.00,
                'dormitorios': 3,
                'banos': 1,
                'imagen_url': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=12),
                'destacado': False,
            },

            # =================================================================
            # 2 TERRENOS
            # =================================================================
            {
                'titulo': 'Terreno Urbano para Proyecto Multifamiliar',
                'tipo_inmueble': 'terreno',
                'operacion': 'venta',
                'distrito': 'El Tambo',
                'precio': 290000.00,
                'descripcion': 'Lote totalmente plano con parámetros urbanísticos para edificar hasta 5 pisos. Título saneado e inscrito en SUNARP, con conexiones de agua, desagüe, luz y fibra óptica.',
                'area_m2': 250.00,
                'dormitorios': None,
                'banos': None,
                'imagen_url': 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=3),
                'destacado': True,
            },
            {
                'titulo': 'Lote Campestre con Vista Panorámica',
                'tipo_inmueble': 'terreno',
                'operacion': 'venta',
                'distrito': 'Chilca',
                'precio': 145000.00,
                'descripcion': 'Excelente oportunidad para casa de campo o huerto familiar en entorno apacible y ecológico. Clima templado y acceso afirmado vehicular a 10 minutos de la plaza principal.',
                'area_m2': 300.00,
                'dormitorios': None,
                'banos': None,
                'imagen_url': 'https://images.unsplash.com/photo-1500076656116-558758c991c1?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=10),
                'destacado': False,
            },

            # =================================================================
            # 2 LOCALES COMERCIALES
            # =================================================================
            {
                'titulo': 'Local Comercial de Alto Tránsito en Calle Real',
                'tipo_inmueble': 'local',
                'operacion': 'alquiler',
                'distrito': 'Huancayo',
                'precio': 4500.00,
                'descripcion': 'Ubicación privilegiada en pleno eje comercial de Huancayo. Frente de vidrio templado, piso de porcelanato de alto tránsito, pozo a tierra y dos baños reglamentarios.',
                'area_m2': 110.00,
                'dormitorios': None,
                'banos': 2,
                'imagen_url': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=2),
                'destacado': True,
            },
            {
                'titulo': 'Oficina Corporativa en Av. Mariscal Castilla',
                'tipo_inmueble': 'local',
                'operacion': 'alquiler',
                'distrito': 'El Tambo',
                'precio': 2200.00,
                'descripcion': 'Local ideal para consultorios médicos, estudio contable o estudio jurídico. Incluye recepción, sala de juntas privada, cableado estructurado y cochera para visitas.',
                'area_m2': 75.00,
                'dormitorios': None,
                'banos': 1,
                'imagen_url': 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=1200&q=80',
                'fecha_publicacion': hoy - timedelta(days=8),
                'destacado': False,
            },
        ]

        # Inserción con get_or_create para idempotencia
        creados = 0
        for item in inmuebles_data:
            obj, created = Producto.objects.get_or_create(
                titulo=item['titulo'],
                defaults=item
            )
            if created:
                creados += 1
                self.stdout.write(self.style.SUCCESS(f"  [+] Registrado: {obj.titulo} ({obj.distrito})"))
            else:
                self.stdout.write(self.style.WARNING(f"  [=] Ya existe: {obj.titulo}"))

        self.stdout.write(self.style.SUCCESS(f"\n¡Poblado completado con éxito! {creados} inmuebles nuevos registrados."))
        self.stdout.write(self.style.NOTICE(f"Total de registros en SQLite: {Producto.objects.count()}"))

