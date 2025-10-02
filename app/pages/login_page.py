import reflex as rx
from app.states.auth_state import AuthState


def login_form() -> rx.Component:
    """Componente del formulario de inicio de sesión."""
    return rx.el.div(
        rx.el.div(
            rx.icon("book-heart", class_name="h-10 w-10 text-indigo-600"),
            rx.el.h2(
                "Iniciar Sesión en PIAR123",
                class_name="text-2xl font-bold text-neutral-800",
            ),
            class_name="flex flex-col items-center text-center gap-4 mb-8",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Correo o Usuario",
                    class_name="block text-sm font-medium text-neutral-600 mb-1",
                ),
                rx.el.input(
                    name="identifier",
                    placeholder="usuario@ejemplo.com o mi_usuario",
                    type_="text",
                    required=True,
                    class_name="w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Contraseña",
                    class_name="block text-sm font-medium text-neutral-600 mb-1",
                ),
                rx.el.input(
                    name="password",
                    placeholder="••••••••",
                    type_="password",
                    required=True,
                    class_name="w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                class_name="mb-6",
            ),
            rx.el.button(
                rx.cond(AuthState.is_loading, rx.spinner(size="2"), "Iniciar Sesión"),
                type="submit",
                disabled=AuthState.is_loading,
                class_name="w-full px-4 py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 transition-colors disabled:bg-indigo-300 disabled:cursor-not-allowed",
            ),
            on_submit=AuthState.sign_in,
            reset_on_submit=False,
            class_name="w-full",
        ),
        class_name="bg-white p-8 rounded-xl shadow-lg border border-neutral-200 w-full max-w-md",
    )


def login_page() -> rx.Component:
    """Página de inicio de sesión."""
    return rx.el.div(
        login_form(),
        class_name="flex items-center justify-center min-h-screen bg-neutral-50 font-['Inter']",
    )