import reflex as rx
from app.state import AppState
from app.components.sidebar import sidebar
from app.pages.dashboard import dashboard_page
from app.pages.students import students_page
from app.pages.piar_formats import piar_formats_page
from app.pages.settings import settings_page
from app.pages.analysis_page import analysis_page


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
        sidebar(),
        rx.el.main(
            rx.el.div(
                rx.match(
                    AppState.active_page,
                    ("Dashboard", dashboard_page()),
                    ("Estudiantes", students_page()),
                    ("Formatos PIAR", piar_formats_page()),
                    ("Análisis Grupal", analysis_page()),
                    ("Configuración", settings_page()),
                    rx.el.p("Página no encontrada."),
                ),
                class_name="p-6 md:p-8 lg:p-12 w-full max-w-7xl mx-auto",
            ),
            class_name="w-full h-screen overflow-y-auto",
        ),
        class_name="flex bg-neutral-50 font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="PIAR123")