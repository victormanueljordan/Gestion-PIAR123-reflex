import reflex as rx


class AuthState(rx.State):
    """Estado para manejar la autenticación de usuarios."""

    users: dict[str, str] = {"admin@piar123.com": "password123", "admin": "password123"}
    in_session: bool = False
    is_loading: bool = False

    @rx.var
    def is_authenticated(self) -> bool:
        """Comprueba si el usuario está autenticado."""
        return self.in_session

    @rx.event
    def sign_in(self, form_data: dict):
        """Maneja el evento de inicio de sesión."""
        self.is_loading = True
        yield
        identifier = form_data.get("identifier", "").strip()
        password = form_data.get("password", "")
        if identifier in self.users and self.users[identifier] == password:
            self.in_session = True
            self.is_loading = False
            return rx.redirect("/")
        else:
            self.is_loading = False
            yield rx.toast.error("Usuario o contraseña inválidos.")

    @rx.event
    def sign_out(self):
        """Maneja el evento de cierre de sesión."""
        self.in_session = False
        return rx.redirect("/login")

    @rx.event
    def check_session(self):
        """Verifica si hay una sesión activa; si no, redirige al login."""
        if not self.is_authenticated:
            return rx.redirect("/login")