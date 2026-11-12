# INMOANDES — Portal Inmobiliario de Huancayo
**Guía Práctica Semana 11 — Desarrollo de Aplicaciones Web (IS093A)**  
**Facultad de Ingeniería de Sistemas — Universidad Nacional del Centro del Perú (UNCP)**  
**Docente:** Unidad II: Desarrollo Web Fullstack  



## 1. Descripción del Proyecto
**InmoAndes** es una aplicación web inmobiliaria moderna desarrollada con **Django 5.1.15**, **Bootstrap 5.3** y **SQLite**, diseñada bajo la arquitectura **MTV (Model-Template-View)**. Permite a los usuarios explorar casas, departamentos, terrenos y locales comerciales en venta y alquiler en los distritos de Huancayo, El Tambo, Chilca y Pilcomayo.

El proyecto cumple al 100 % con los requisitos obligatorios de la Guía Práctica de la Semana 11, integrando vistas basadas en funciones (FBV), vistas basadas en clases (CBV `ListView`), herencia de plantillas modular con Django Template Language (DTL), y el modelo de persistencia denominado literalmente `Producto`.



## 2. Tecnologías Utilizadas
- **Lenguaje:** Python 3.11+
- **Framework Backend:** Django 5.1.15
- **Base de Datos:** SQLite 3
- **Frontend & UI:** HTML5 semántico, CSS3 personalizado (CSS Custom Properties), Bootstrap 5.3.3, Bootstrap Icons 1.11.3
- **Tipografías:** Manrope (Títulos y precios) e Inter (Cuerpo y metadatos)
- **Control de Versiones:** Git & GitHub (con exclusión preventiva de `db.sqlite3` y entornos virtuales)



## 3. Arquitectura MTV (Model - Template - View)


        USUARIO (Navegador Web)
                   │
                   ▼  HTTP Request
        config/urls.py  ──include()──>  propiedades/urls.py
                                                │
                          ┌─────────────────────┴─────────────────────┐
                          ▼                                           ▼
                 FBV: home(request)                   CBV: PropiedadListView(ListView)
                 (Ruta: '/')                          (Ruta: '/propiedades/')
                          │                                           │
                          ▼                                           ▼
                 Consulta ORM Destacados               Consulta ORM con Filtros GET
             (Producto.objects.filter)              (Producto.objects.filter(...))
                          │                                           │
                          └─────────────────────┬─────────────────────┘
                                                ▼
                                         SQLite (db.sqlite3)
                                      [Tabla: propiedades_producto]
                                                │
                                                ▼ Contexto DTL
                                     propiedades/templates/
                                       ├── base.html (Maestra)
                                       ├── home.html (extends)
                                       └── catalogo.html (extends)
                                                │
                                                ▼  HTTP Response (HTML Renderizado)
                                        USUARIO (Navegador)


- **Model (`propiedades/models.py`):** Define el modelo `Producto` con sus tipos de campos, opciones (`choices`), metadatos y método `__str__()`. Administra la persistencia en SQLite mediante el ORM.
- **Template (`propiedades/templates/propiedades/`):** Capa de presentación visual que utiliza herencia (`{% extends %}`), bloques (`{% block %}`), bucles (`{% for %}` con `{% empty %}`), condicionales (`{% if %}`), y filtros (`|title`, `|date`, `|floatformat`).
- **View (`propiedades/views.py`):** Capa de control y despacho HTTP. Implementa tanto una **FBV (`home`)** como una **CBV (`PropiedadListView`)**.



## 4. Estructura de Directorios del Proyecto


SEMANA11_1/
│
├── manage.py                          # CLI orquestador de Django
├── requirements.txt                   # Dependencias congeladas (Django 5.1.15, etc.)
├── .gitignore                         # Excluye venv/, db.sqlite3, __pycache__/
├── README.md                          # Documentación técnica y académica
│
├── config/                            # Paquete de configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                    # Registro de 'propiedades', es-pe, Lima
│   ├── urls.py                        # include('propiedades.urls')
│   └── wsgi.py
│
└── propiedades/                       # Aplicación Inmobiliaria
    ├── admin.py
    ├── apps.py
    ├── models.py                      # Modelo obligatorio 'Producto' (ORM)
    ├── tests.py                       # Suite de pruebas unitarias (6 tests)
    ├── urls.py                        # Espacio de nombres: app_name = 'propiedades'
    ├── views.py                       # FBV home() y CBV PropiedadListView
    │
    ├── management/
    │   └── commands/
    │       └── poblar_inmuebles.py    # Comando reproducible para cargar 12 inmuebles
    │
    ├── migrations/
    │   └── 0001_initial.py            # Migración inicial del modelo Producto
    │
    ├── static/
    │   └── propiedades/
    │       └── css/
    │           └── estilos.css        # Variables CSS, componentes, responsive
    │
    └── templates/
        └── propiedades/
            ├── base.html              # Plantilla base (Navbar, Footer, Bootstrap)
            ├── home.html              # Plantilla de Inicio (Hero, Buscador, Destacados)
            └── catalogo.html          # Plantilla del Catálogo (Filtros, Grid, Empty)




## 5. Instrucciones de Instalación y Ejecución Local

### Paso 1: Clonar el repositorio y acceder a la carpeta

git clone <URL_DE_TU_REPOSITORIO_GITHUB>
cd SEMANA11_1


### Paso 2: Crear y activar el entorno virtual
En Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


### Paso 3: Instalar dependencias

pip install -r requirements.txt


### Paso 4: Ejecutar migraciones de la base de datos

python manage.py check
python manage.py makemigrations propiedades
python manage.py migrate


### Paso 5: Poblar los 12 inmuebles de demostración (Huancayo)

python manage.py poblar_inmuebles


### Paso 6: Ejecutar las pruebas unitarias automatizadas

python manage.py test

*Resultado esperado:* `Ran 6 tests in ... OK`.

### Paso 7: Iniciar el servidor de desarrollo

python manage.py runserver

Abrir en el navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 6. Endpoints y Rutas Implementadas

| URL | Nombre de Ruta (Reverse) | Tipo de Vista | Función / Propósito |
| :--- | :--- | :--- | :--- |
| `/` | `propiedades:home` | FBV (`home`) | Portada principal, Hero, Buscador GET, Categorías y Propiedades destacadas (ORM). |
| `/propiedades/` | `propiedades:catalogo` | CBV (`PropiedadListView`) | Catálogo general de inmuebles con filtros por tipo, distrito y modalidad mediante el ORM. |
| `/admin/` | `admin:index` | Django Admin | Panel administrativo de Django. |


## 7. Declaración de Uso Controlado de IA (Regla de la Guía)
En estricto cumplimiento de la regla de laboratorio (75 % de desarrollo manual):
- **Asistencia recibida:** Explicación teórica de CBV (`ListView`) vs FBV, depuración de configuración de plantillas, formulación de consultas ORM de filtrado dinámico y diseño de tokens CSS.
- **Formato de registro de correcciones asistidas:**  
  - `# IA: [Configuración inicial mostraba default_urlconf] → Solución manual: [Configuración desacoplada en config/urls.py delegando a propiedades.urls con include()]`  
  - `# IA: [Filtros GET no preservaban selección] → Solución manual: [Uso de request.GET.<campo> en atributos selected de catalogo.html]`


## 8. Evidencias Verificadas del Ejercicio

1. **`python manage.py check`:** `0 issues`.
2. **`python manage.py showmigrations propiedades`:** `[X] 0001_initial`.
3. **`python manage.py test`:** 6 pruebas unitarias aprobadas exitosamente.
4. **Base de Datos SQLite:** 12 registros de demostración activos (4 casas, 4 departamentos, 2 terrenos, 2 locales comerciales) con imágenes y metadatos reales.
5. **Filtros verificados:** Consultas por `tipo`, `distrito` y `operacion` evaluadas mediante el ORM con Lazy Evaluation.
6. **Seguridad y Git:** `db.sqlite3` y `venv/` están correctamente ignorados en `.gitignore`.
