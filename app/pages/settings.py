import reflex as rx
from app.states.settings_state import SettingsState


def form_input(
    label: str, placeholder: str, name: str, input_type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-neutral-700"),
        rx.el.input(
            type=input_type,
            name=name,
            placeholder=placeholder,
            default_value=SettingsState.form_data[name],
            class_name="mt-1 block w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
        ),
        class_name="w-full",
    )


def form_switch(label: str, name: str) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            rx.el.span(label, class_name="text-sm font-medium text-neutral-700"),
            rx.el.div(
                rx.el.input(
                    type="checkbox",
                    name=name,
                    class_name="sr-only peer",
                    is_checked=SettingsState.form_data[name],
                ),
                rx.el.div(
                    class_name="w-11 h-6 bg-neutral-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-indigo-300 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-neutral-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"
                ),
                class_name="relative",
            ),
            class_name="flex items-center justify-between w-full",
        )
    )


def settings_page() -> rx.Component:
    """Page for adjusting app and profile settings."""
    return rx.el.div(
        rx.el.h1("Configuración", class_name="text-3xl font-bold text-neutral-800"),
        rx.el.p(
            "Ajuste la configuración de la aplicación y su perfil.",
            class_name="text-neutral-600 mt-1",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Información del Perfil",
                        class_name="text-lg font-semibold text-neutral-800 border-b pb-3",
                    ),
                    rx.el.div(
                        form_input("Nombre Completo", "Su nombre", "name"),
                        form_input(
                            "Correo Electrónico", "su@email.com", "email", "email"
                        ),
                        class_name="mt-4 grid grid-cols-1 md:grid-cols-2 gap-6",
                    ),
                    class_name="p-6 bg-white border border-neutral-200 rounded-xl shadow-sm",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Notificaciones",
                        class_name="text-lg font-semibold text-neutral-800 border-b pb-3",
                    ),
                    rx.el.div(
                        form_switch(
                            "Notificaciones Generales", "notifications_general"
                        ),
                        form_switch(
                            "Actualizaciones de Producto", "notifications_updates"
                        ),
                        class_name="mt-4 flex flex-col gap-4",
                    ),
                    class_name="mt-6 p-6 bg-white border border-neutral-200 rounded-xl shadow-sm",
                ),
                rx.el.div(
                    rx.el.button(
                        "Guardar Cambios",
                        type="submit",
                        class_name="px-6 py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 transition-colors",
                    ),
                    class_name="mt-6 flex justify-end",
                ),
            ),
            on_submit=SettingsState.handle_submit,
            class_name="mt-8 max-w-4xl mx-auto",
        ),
        class_name="w-full",
    )