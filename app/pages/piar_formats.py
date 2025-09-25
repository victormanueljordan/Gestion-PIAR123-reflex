import reflex as rx
from app.states.piar_state import PiarState, PiarFormat
from app.pages.piar_form import piar_form_page


def piar_actions(piar: PiarFormat) -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("download", class_name="h-4 w-4"),
            on_click=PiarState.export_piar_to_pdf,
            class_name="p-2 hover:bg-neutral-200 rounded-md",
        ),
        rx.el.button(
            rx.icon("pencil", class_name="h-4 w-4"),
            on_click=lambda: PiarState.select_piar_for_editing(piar),
            class_name="p-2 hover:bg-neutral-200 rounded-md",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("bot", class_name="h-4 w-4"),
                on_click=lambda: PiarState.open_assistant_form(piar),
                class_name="p-2 hover:bg-neutral-200 rounded-md",
            ),
            title="Asistente PIAR",
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


def piar_card(piar: PiarFormat) -> rx.Component:
    """Displays a single PIAR format as a card."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    piar["student_name"],
                    class_name="text-lg font-bold text-neutral-800",
                ),
                rx.el.p(f"ID: {piar['id']}", class_name="text-sm text-neutral-500"),
            ),
            status_badge(piar["status"]),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p("Fecha de creación", class_name="text-xs text-neutral-500"),
                rx.el.p(piar["creation_date"], class_name="font-medium text-sm"),
            ),
            rx.el.div(
                rx.el.p("Última modificación", class_name="text-xs text-neutral-500"),
                rx.el.p(
                    f"{piar['last_modified_date']} por {piar['last_modified_by']}",
                    class_name="font-medium text-sm",
                ),
            ),
            class_name="grid grid-cols-2 gap-4 mb-4",
        ),
        rx.el.div(
            piar_actions(piar),
            class_name="flex justify-end pt-4 border-t border-neutral-100",
        ),
        class_name="bg-white p-6 rounded-xl border border-neutral-200 shadow-sm hover:shadow-lg transition-shadow",
    )


def piar_list_view() -> rx.Component:
    """The view for listing all PIAR formats."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Formatos PIAR", class_name="text-3xl font-bold text-neutral-800"
                ),
                rx.el.p(
                    "Edite y gestione los formatos PIAR de los estudiantes.",
                    class_name="text-neutral-600 mt-1",
                ),
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    placeholder="Buscar por nombre de estudiante...",
                    on_change=PiarState.set_search_query_piar.debounce(300),
                    class_name="w-full md:w-1/3 px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                rx.el.select(
                    rx.foreach(
                        PiarState.status_options_piar,
                        lambda status: rx.el.option(status, value=status),
                    ),
                    on_change=PiarState.set_status_filter_piar,
                    default_value="",
                    class_name="w-full md:w-1/4 px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                class_name="flex flex-col md:flex-row gap-4 mb-6",
            ),
            class_name="mt-8",
        ),
        rx.el.div(
            rx.foreach(PiarState.paginated_piar_formats, piar_card),
            class_name="mt-6 grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6",
        ),
        rx.el.div(
            rx.el.p(
                f"Página {PiarState.current_page_piar} de {PiarState.total_pages_piar}",
                class_name="text-sm text-neutral-600",
            ),
            rx.el.div(
                rx.el.button(
                    "Anterior",
                    on_click=PiarState.prev_page_piar,
                    disabled=PiarState.current_page_piar <= 1,
                    class_name="px-4 py-2 text-sm font-semibold bg-white border border-neutral-300 rounded-md shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:cursor-not-allowed",
                ),
                rx.el.button(
                    "Siguiente",
                    on_click=PiarState.next_page_piar,
                    disabled=PiarState.current_page_piar >= PiarState.total_pages_piar,
                    class_name="px-4 py-2 text-sm font-semibold bg-white border border-neutral-300 rounded-md shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:cursor-not-allowed",
                ),
                class_name="flex gap-2",
            ),
            class_name="flex justify-between items-center mt-8",
        ),
        class_name="w-full",
    )


from .piar_assistant_page import piar_assistant_page


def piar_formats_page() -> rx.Component:
    """Page for managing PIAR formats."""
    return rx.el.div(
        rx.cond(
            PiarState.show_assistant_form,
            piar_assistant_page(),
            rx.cond(
                PiarState.show_piar_form & PiarState.selected_piar.is_not_none(),
                piar_form_page(),
                piar_list_view(),
            ),
        ),
        class_name="w-full",
    )