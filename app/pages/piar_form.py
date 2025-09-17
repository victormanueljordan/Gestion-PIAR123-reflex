import reflex as rx
from app.states.piar_state import PiarState


def form_section(title: str, content: rx.Component) -> rx.Component:
    """A section in the PIAR form."""
    return rx.el.div(
        rx.el.h2(
            title,
            class_name="text-xl font-semibold text-neutral-800 border-b pb-3 mb-6",
        ),
        content,
        class_name="p-6 bg-white border border-neutral-200 rounded-xl shadow-sm mb-6",
    )


def piar_form_page() -> rx.Component:
    """The full-screen form for creating/editing a PIAR."""
    sections = [
        "1. Caracterización del estudiante",
        "2. Valoración pedagógica",
        "3. Valoración interdisciplinar (si aplica)",
        "4. Barreras para el aprendizaje y la participación",
        "5. Ajustes razonables",
        "6. Estrategias pedagógicas",
        "7. Seguimiento y evaluación",
        "8. Acta de acuerdos y compromisos",
    ]
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Diligenciar Formato PIAR",
                    class_name="text-3xl font-bold text-neutral-800",
                ),
                rx.el.p(
                    f"Editando PIAR para: {PiarState.selected_piar['student_name']}",
                    class_name="text-neutral-600 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("arrow-left", class_name="h-5 w-5"),
                "Volver a la lista",
                on_click=PiarState.return_to_piar_list,
                class_name="flex items-center gap-2 px-4 py-2 bg-neutral-200 text-neutral-800 font-semibold rounded-lg hover:bg-neutral-300 transition-colors",
            ),
            class_name="flex items-center justify-between mb-8",
        ),
        rx.foreach(
            sections,
            lambda section: form_section(
                section,
                rx.el.p("Contenido de la sección...", class_name="text-neutral-500"),
            ),
        ),
        class_name="w-full max-w-5xl mx-auto",
    )