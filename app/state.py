import reflex as rx
from typing import Literal

Page = Literal["Dashboard", "Estudiantes", "Formatos PIAR", "Configuración"]


class AppState(rx.State):
    """The main application state."""

    active_page: Page = "Dashboard"
    sidebar_open: bool = True

    @rx.event
    def set_active_page(self, page: Page):
        """Sets the currently active page."""
        self.active_page = page

    @rx.event
    def toggle_sidebar(self):
        """Toggles the visibility of the sidebar."""
        self.sidebar_open = not self.sidebar_open