import reflex as rx
from app.state import AppState
from app.states.auth_state import AuthState
from app.components.sidebar import sidebar
from app.pages.dashboard import dashboard_page
from app.pages.students import students_page
from app.pages.piar_formats import piar_formats_page
from app.pages.settings import settings_page
from app.pages.analysis_page import analysis_page
from app.pages.login_page import login_page


def protected_page(page_content: rx.Component) -> rx.Component:
    """Una página protegida que requiere autenticación."""
    return rx.cond(AuthState.is_authenticated, page_content, login_page())


def index() -> rx.Component:
    """Vista principal de la aplicación PIAR123."""
    main_content = rx.el.div(
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
    return protected_page(main_content)


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
app.add_page(index, title="PIAR123", on_load=AuthState.check_session)
app.add_page(login_page, route="/login", title="Iniciar Sesión")