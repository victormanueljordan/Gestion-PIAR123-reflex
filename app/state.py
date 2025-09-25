import reflex as rx
from typing import Literal

Page = Literal[
    "Dashboard", "Estudiantes", "Formatos PIAR", "Análisis Grupal", "Configuración"
]


class AppState(rx.State):
    """Estado principal de la aplicación PIAR123.

    Esta clase maneja todo el estado global de la aplicación, incluyendo:
    - La página actualmente activa en el sistema de navegación
    - El estado de visibilidad del sidebar de navegación

    Attributes:
        active_page (Page): Página actualmente visible en la aplicación.
                           Por defecto es "Dashboard".
        sidebar_open (bool): Estado de visibilidad del sidebar.
                            True = visible, False = oculto.
    """

    active_page: Page = "Dashboard"
    sidebar_open: bool = True

    @rx.event
    def set_active_page(self, page: Page):
        """Establece la página actualmente activa en la aplicación.

        Este método es llamado cuando el usuario navega a una nueva página
        a través del sidebar o cualquier otro elemento de navegación.

        Args:
            page (Page): Nombre de la página a activar. Debe ser uno de los
                        valores definidos en el tipo Page.

        Note:
            Este método actualiza automáticamente la interfaz para mostrar
            el contenido de la página seleccionada.
        """
        self.active_page = page

    @rx.event
    def toggle_sidebar(self):
        """Alterna la visibilidad del sidebar de navegación.

        Este método cambia el estado del sidebar entre visible y oculto.
        Útil para dispositivos móviles o cuando se necesita más espacio
        para el contenido principal.

        Note:
            El estado se invierte automáticamente: si está abierto se cierra
            y viceversa. La interfaz se actualiza inmediatamente.
        """
        self.sidebar_open = not self.sidebar_open