import reflex as rx
from app.state import AppState, Page


def sidebar_item(name: Page, icon: str) -> rx.Component:
    """A single item in the sidebar."""
    return rx.el.a(
        rx.el.div(
            rx.icon(tag=icon, class_name="h-5 w-5"),
            rx.el.span(
                name,
                class_name=rx.cond(
                    AppState.sidebar_open,
                    "opacity-100 translate-x-0",
                    "opacity-0 -translate-x-3",
                ),
                style={
                    "transition": "opacity 0.2s ease-in-out, transform 0.2s ease-in-out",
                    "transition_delay": "0.1s",
                },
            ),
            class_name="flex items-center gap-3",
        ),
        on_click=lambda: AppState.set_active_page(name),
        class_name=rx.cond(
            AppState.active_page == name,
            "flex items-center p-3 rounded-lg bg-indigo-50 text-indigo-600 font-semibold cursor-pointer transition-colors duration-200",
            "flex items-center p-3 rounded-lg text-neutral-600 hover:bg-neutral-100 hover:text-neutral-800 font-medium cursor-pointer transition-colors duration-200",
        ),
        width=rx.cond(AppState.sidebar_open, "100%", "fit-content"),
    )


def sidebar() -> rx.Component:
    """The main sidebar component for navigation."""
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("book-marked", class_name="h-8 w-8 text-indigo-600"),
                    rx.el.h1(
                        "PIAR123",
                        class_name="text-2xl font-bold text-neutral-800",
                        style={
                            "transition": "opacity 0.2s ease-in-out, width 0.3s ease-in-out",
                            "opacity": rx.cond(AppState.sidebar_open, "1", "0"),
                            "width": rx.cond(AppState.sidebar_open, "auto", "0"),
                        },
                    ),
                    class_name="flex items-center gap-3 overflow-hidden",
                ),
                rx.el.button(
                    rx.icon(
                        tag="chevrons-left",
                        class_name="h-5 w-5 text-neutral-500",
                        style={
                            "transform": rx.cond(
                                AppState.sidebar_open, "rotate(0deg)", "rotate(180deg)"
                            ),
                            "transition": "transform 0.3s ease",
                        },
                    ),
                    on_click=AppState.toggle_sidebar,
                    class_name="p-2 rounded-lg hover:bg-neutral-100",
                ),
                class_name="flex items-center justify-between p-4 border-b border-neutral-200",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "layout-dashboard"),
                sidebar_item("Estudiantes", "users"),
                sidebar_item("Formatos PIAR", "file-text"),
                sidebar_item("Configuración", "settings-2"),
                class_name="flex flex-col gap-2 p-4",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="https://api.dicebear.com/9.x/initials/svg?seed=Admin",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.p(
                        "Admin User",
                        class_name="font-semibold text-sm text-neutral-800",
                    ),
                    rx.el.p("admin@piar123.com", class_name="text-xs text-neutral-500"),
                    class_name="flex flex-col",
                    style={
                        "transition": "opacity 0.2s ease-in-out, width 0.3s ease-in-out",
                        "opacity": rx.cond(AppState.sidebar_open, "1", "0"),
                        "width": rx.cond(AppState.sidebar_open, "auto", "0"),
                    },
                ),
                class_name="flex items-center gap-3 p-4 overflow-hidden",
            ),
            class_name="border-t border-neutral-200",
        ),
        class_name="flex flex-col justify-between h-screen bg-white border-r border-neutral-200 transition-width duration-300 ease-in-out",
        width=rx.cond(AppState.sidebar_open, "280px", "80px"),
    )