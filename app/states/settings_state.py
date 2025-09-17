import reflex as rx


class SettingsState(rx.State):
    """State for the settings page."""

    form_data: dict = {
        "name": "Admin User",
        "email": "admin@piar123.com",
        "notifications_general": True,
        "notifications_updates": False,
    }

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        return rx.toast("Configuración guardada exitosamente!")