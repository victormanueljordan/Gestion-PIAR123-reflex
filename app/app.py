# Importaciones principales de Reflex y componentes del proyecto
import reflex as rx
from app.state import AppState  # Estado global de la aplicación
from app.components.sidebar import sidebar  # Componente de navegación lateral
# Importación de todas las páginas de la aplicación
from app.pages.dashboard import dashboard_page
from app.pages.students import students_page
from app.pages.piar_formats import piar_formats_page
from app.pages.settings import settings_page


def index() -> rx.Component:
    """Vista principal de la aplicación PIAR123.
    
    Esta función define el layout principal que contiene:
    - Sidebar de navegación lateral
    - Área de contenido principal con sistema de enrutamiento
    
    Returns:
        rx.Component: Componente principal con layout flex que incluye
                     sidebar y contenido dinámico basado en el estado activo
    """
    return rx.el.div(
        # Componente de navegación lateral fijo
        sidebar(),
        # Área principal de contenido
        rx.el.main(
            rx.el.div(
                # Sistema de enrutamiento basado en el estado activo
                # Utiliza rx.match para renderizar la página correspondiente
                rx.match(
                    AppState.active_page,  # Variable de estado que determina la página activa
                    ("Dashboard", dashboard_page()),  # Página principal con estadísticas
                    ("Estudiantes", students_page()),  # Gestión de estudiantes
                    ("Formatos PIAR", piar_formats_page()),  # Formularios PIAR
                    ("Configuración", settings_page()),  # Configuración de la app
                    rx.el.p("Página no encontrada."),  # Fallback para rutas no válidas
                ),
                # Contenedor con padding responsivo y ancho máximo centrado
                class_name="p-6 md:p-8 lg:p-12 w-full max-w-7xl mx-auto",
            ),
            # Área principal con scroll vertical y altura completa
            class_name="w-full h-screen overflow-y-auto",
        ),
        # Layout flex horizontal con fondo gris claro y fuente Inter
        class_name="flex bg-neutral-50 font-['Inter']",
    )


# Configuración principal de la aplicación Reflex
app = rx.App(
    # Tema de la aplicación configurado en modo claro
    theme=rx.theme(appearance="light"),
    # Componentes del head para optimización de fuentes
    head_components=[
        # Preconexión a Google Fonts para mejorar rendimiento
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        # Carga de la fuente Inter con diferentes pesos
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
# Registro de la página principal con título de la aplicación
app.add_page(index, title="PIAR123")