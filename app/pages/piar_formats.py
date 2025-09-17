import reflex as rx
from app.states.piar_state import PiarState, PiarFormat


def piar_actions() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("eye", class_name="h-4 w-4"),
            class_name="p-2 hover:bg-neutral-200 rounded-md",
        ),
        rx.el.button(
            rx.icon("pencil", class_name="h-4 w-4"),
            class_name="p-2 hover:bg-neutral-200 rounded-md",
        ),
        rx.el.button(
            rx.icon("trash-2", class_name="h-4 w-4 text-red-500"),
            class_name="p-2 hover:bg-neutral-200 rounded-md",
        ),
        class_name="flex items-center gap-2",
    )


def status_badge(status: rx.Var[str]) -> rx.Component:
    return rx.el.span(
        status,
        class_name=rx.match(
            status,
            (
                "Completado",
                "px-2 py-1 text-xs font-semibold text-green-800 bg-green-100 rounded-full",
            ),
            (
                "En Progreso",
                "px-2 py-1 text-xs font-semibold text-blue-800 bg-blue-100 rounded-full",
            ),
            (
                "Pendiente",
                "px-2 py-1 text-xs font-semibold text-yellow-800 bg-yellow-100 rounded-full",
            ),
            "px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-100 rounded-full",
        ),
    )


def piar_row(piar: PiarFormat) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.p(
                    piar["student_name"], class_name="font-semibold text-neutral-800"
                ),
                rx.el.p(f"ID: {piar['id']}", class_name="text-sm text-neutral-500"),
                class_name="flex flex-col",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(piar["creation_date"], class_name="px-6 py-4 text-neutral-600"),
        rx.el.td(status_badge(piar["status"]), class_name="px-6 py-4"),
        rx.el.td(piar_actions(), class_name="px-6 py-4 text-right"),
        class_name="border-b border-neutral-200 hover:bg-neutral-100",
    )


def piar_formats_page() -> rx.Component:
    """Page for managing PIAR formats."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Formatos PIAR", class_name="text-3xl font-bold text-neutral-800"
                ),
                rx.el.p(
                    "Cree, edite y gestione los formatos PIAR.",
                    class_name="text-neutral-600 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("circle_plus", class_name="h-5 w-5"),
                "Crear Nuevo PIAR",
                class_name="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 transition-colors",
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Estudiante",
                                class_name="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Fecha Creación",
                                class_name="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Estado",
                                class_name="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider",
                            ),
                            rx.el.th("", class_name="px-6 py-3"),
                        )
                    ),
                    rx.el.tbody(rx.foreach(PiarState.piar_formats, piar_row)),
                    class_name="min-w-full bg-white",
                ),
                class_name="overflow-hidden border border-neutral-200 rounded-xl",
            ),
            class_name="mt-8",
        ),
        class_name="w-full",
    )