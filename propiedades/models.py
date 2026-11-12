from django.db import models
from django.utils import timezone

class Producto(models.Model):
    """
    Modelo obligatorio de la Guía Práctica de la Semana 11 (UNCP - FIS).
    Representa publicaciones de propiedades inmobiliarias en el portal InmoAndes.
    """

    # Opciones predefinidas para validación y selects
    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('terreno', 'Terreno'),
        ('local', 'Local Comercial'),
    ]

    OPERACION_CHOICES = [
        ('venta', 'Venta'),
        ('alquiler', 'Alquiler'),
    ]

    DISTRITO_CHOICES = [
        ('Huancayo', 'Huancayo'),
        ('El Tambo', 'El Tambo'),
        ('Chilca', 'Chilca'),
        ('Pilcomayo', 'Pilcomayo'),
    ]

    # 1. Identificación y clasificación
    titulo = models.CharField(
        max_length=200, 
        verbose_name="Título del inmueble"
    )
    tipo_inmueble = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES, 
        verbose_name="Tipo de inmueble"
    )
    operacion = models.CharField(
        max_length=10, 
        choices=OPERACION_CHOICES, 
        verbose_name="Modalidad de operación"
    )
    distrito = models.CharField(
        max_length=50, 
        choices=DISTRITO_CHOICES, 
        verbose_name="Distrito"
    )

    # 2. Aspectos económicos y descriptivos
    precio = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        verbose_name="Precio (S/)"
    )
    descripcion = models.TextField(
        verbose_name="Descripción detallada"
    )

    # 3. Metadatos físicos y distribución
    area_m2 = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        verbose_name="Área total (m²)"
    )
    dormitorios = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        verbose_name="Número de dormitorios"
    )
    banos = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        verbose_name="Número de baños"
    )

    # 4. Multimedia y control temporal
    imagen_url = models.URLField(
        max_length=500, 
        blank=True, 
        default="", 
        verbose_name="URL de imagen del inmueble"
    )
    fecha_publicacion = models.DateField(
        default=timezone.now, 
        verbose_name="Fecha de publicación"
    )
    destacado = models.BooleanField(
        default=False, 
        verbose_name="¿Es propiedad destacada?"
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_publicacion', '-id']

    def __str__(self):
        """
        Representación textual del inmueble para Django Admin y Django Shell.
        """
        return f"{self.titulo} | {self.get_operacion_display()} en {self.distrito} - S/ {self.precio}"
