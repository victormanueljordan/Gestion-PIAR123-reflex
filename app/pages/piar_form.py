import reflex as rx
from app.states.piar_state import PiarState


def item_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
            on_click=PiarState.close_item_modal,
        ),
        rx.el.div(
            rx.el.form(
                rx.el.h2(
                    rx.cond(
                        PiarState.editing_item,
                        "Editar Registro",
                        "Añadir Nuevo Registro",
                    ),
                    class_name="text-lg font-bold text-neutral-800 mb-4 p-6 border-b",
                ),
                rx.el.div(
                    rx.el.label("Materia/Área", class_name="text-sm font-medium"),
                    rx.el.select(
                        rx.foreach(
                            PiarState.materias, lambda m: rx.el.option(m, value=m)
                        ),
                        name="materia",
                        default_value=PiarState.editing_item["materia"].to(str),
                        class_name="mt-1 w-full p-2 border rounded-md",
                        disabled=PiarState.is_final,
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Periodo", class_name="text-sm font-medium"),
                    rx.el.select(
                        rx.foreach(
                            PiarState.periodos, lambda p: rx.el.option(p, value=p)
                        ),
                        name="periodo",
                        default_value=PiarState.editing_item["periodo"].to(str),
                        class_name="mt-1 w-full p-2 border rounded-md",
                        disabled=PiarState.is_final,
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Descripción", class_name="text-sm font-medium"),
                    rx.el.textarea(
                        name="descripcion",
                        default_value=PiarState.editing_item["descripcion"].to(str),
                        class_name="mt-1 w-full p-2 border rounded-md",
                        rows=4,
                        placeholder="Describa el registro...",
                        disabled=PiarState.is_final,
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancelar",
                        type_="button",
                        on_click=PiarState.close_item_modal,
                        class_name="px-4 py-2 bg-neutral-200 text-neutral-800 font-semibold rounded-lg",
                    ),
                    rx.el.button(
                        "Guardar",
                        type_="submit",
                        class_name="px-4 py-2 bg-indigo-600 text-white font-semibold rounded-lg",
                    ),
                    class_name="flex justify-end gap-4 p-6 border-t",
                ),
                on_submit=PiarState.save_item,
                reset_on_submit=True,
                class_name="p-6",
            ),
            class_name="bg-white rounded-xl shadow-2xl w-full max-w-lg flex flex-col z-50",
        ),
        open=PiarState.show_item_modal,
        class_name="fixed inset-0 open:flex items-center justify-center p-4 z-50",
    )


def text_area_field(
    label: str, placeholder: str, value: rx.Var, on_change: rx.event.EventHandler
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-sm font-medium text-neutral-700 mb-1"
        ),
        rx.el.textarea(
            placeholder=placeholder,
            on_change=on_change,
            class_name="w-full p-2 border border-neutral-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500",
            rows=5,
            disabled=PiarState.is_final,
            default_value=value,
        ),
        class_name="mb-4",
    )


def single_entry_section(section_name: str, fields: dict) -> rx.Component:
    return rx.el.div(
        rx.foreach(
            list(fields.items()),
            lambda field: text_area_field(
                field[1]["label"],
                field[1]["placeholder"],
                getattr(PiarState, section_name)[field[0]],
                lambda val: PiarState.update_single_entry_field(
                    section_name, field[0], val
                ),
            ),
        )
    )


def multi_entry_section(section_key: str, items: rx.Var[list]) -> rx.Component:
    columns = ["Materia/Área", "Periodo", "Descripción", "Acciones"]
    return rx.el.div(
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.foreach(
                            columns,
                            lambda col: rx.el.th(
                                col,
                                class_name="px-4 py-2 text-left text-sm font-semibold",
                            ),
                        )
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        items,
                        lambda item: rx.el.tr(
                            rx.el.td(item["materia"], class_name="px-4 py-2 border-t"),
                            rx.el.td(item["periodo"], class_name="px-4 py-2 border-t"),
                            rx.el.td(
                                item["descripcion"],
                                class_name="px-4 py-2 border-t max-w-xs truncate",
                            ),
                            rx.el.td(
                                rx.el.div(
                                    rx.el.button(
                                        rx.icon(tag="pencil", size=16),
                                        on_click=lambda: PiarState.open_item_modal(
                                            section_key, item
                                        ),
                                        disabled=PiarState.is_final,
                                        class_name="p-1 hover:bg-neutral-200 rounded",
                                    ),
                                    rx.el.button(
                                        rx.icon(tag="trash-2", size=16),
                                        on_click=lambda: PiarState.delete_item(
                                            section_key, item["id"]
                                        ),
                                        disabled=PiarState.is_final,
                                        class_name="p-1 hover:bg-red-100 text-red-500 rounded",
                                    ),
                                    class_name="flex gap-2",
                                ),
                                class_name="px-4 py-2 border-t",
                            ),
                            class_name="hover:bg-neutral-50",
                        ),
                    )
                ),
                class_name="w-full border-collapse",
            ),
            class_name="overflow-x-auto rounded-lg border",
        ),
        rx.el.button(
            "Añadir Registro",
            on_click=lambda: PiarState.open_item_modal(section_key),
            disabled=PiarState.is_final,
            class_name="mt-4 px-4 py-2 bg-indigo-500 text-white font-semibold rounded-lg text-sm hover:bg-indigo-600",
        ),
    )


def accordion_section(
    title: rx.Var[str], section_key: str, content: rx.Component
) -> rx.Component:
    is_open = PiarState.active_accordion.contains(section_key)
    return rx.el.div(
        rx.el.button(
            rx.el.div(
                rx.el.h2(title, class_name="text-lg font-semibold text-neutral-800"),
                rx.icon(tag=rx.cond(is_open, "chevron-up", "chevron-down")),
                class_name="flex justify-between items-center w-full",
            ),
            on_click=lambda: PiarState.toggle_accordion(section_key),
            class_name="w-full p-4 text-left bg-neutral-100 rounded-t-lg",
        ),
        rx.cond(is_open, rx.el.div(content, class_name="p-6"), rx.fragment()),
        class_name="bg-white border border-neutral-200 rounded-lg shadow-sm mb-4",
    )


def piar_form_page() -> rx.Component:
    return rx.el.div(
        item_modal(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Diligenciar Formato PIAR",
                    class_name="text-3xl font-bold text-neutral-800",
                ),
                rx.el.p(
                    f"Editando PIAR para: {PiarState.selected_piar['student_name']} - Estado: ",
                    rx.el.span(
                        PiarState.piar_status,
                        class_name=rx.cond(
                            PiarState.is_final,
                            "font-bold text-red-600",
                            "font-bold text-green-600",
                        ),
                    ),
                    class_name="text-neutral-600 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("arrow-left", class_name="h-5 w-5"),
                "Volver",
                on_click=PiarState.return_to_piar_list,
                class_name="flex items-center gap-2 px-4 py-2 bg-neutral-200 text-neutral-800 font-semibold rounded-lg hover:bg-neutral-300",
            ),
            class_name="flex items-start justify-between mb-8",
        ),
        accordion_section(
            "1. Caracterización del estudiante",
            "caracterizacion",
            single_entry_section(
                "caracterizacion",
                {
                    "descripcion_general": {
                        "label": "Descripción general del estudiante",
                        "placeholder": "Fortalezas, gustos, intereses, motivaciones...",
                    },
                    "talentos_intereses": {
                        "label": "Talentos e intereses especiales",
                        "placeholder": "Actividades en las que destaca o disfruta...",
                    },
                },
            ),
        ),
        accordion_section(
            "2. Valoración pedagógica",
            "valoracion_pedagogica",
            single_entry_section(
                "valoracion_pedagogica",
                {
                    "desempeno_academico": {
                        "label": "Desempeño académico general",
                        "placeholder": "Cómo le va en las diferentes áreas...",
                    },
                    "competencias_curriculares": {
                        "label": "Competencias curriculares",
                        "placeholder": "Habilidades y conocimientos por área...",
                    },
                },
            ),
        ),
        accordion_section(
            "3. Valoración interdisciplinar (si aplica)",
            "valoracion_interdisciplinar",
            single_entry_section(
                "valoracion_interdisciplinar",
                {
                    "fonoaudiologia": {
                        "label": "Fonoaudiología",
                        "placeholder": "Informe o resumen...",
                    },
                    "terapia_ocupacional": {
                        "label": "Terapia Ocupacional",
                        "placeholder": "Informe o resumen...",
                    },
                    "psicologia": {
                        "label": "Psicología",
                        "placeholder": "Informe o resumen...",
                    },
                },
            ),
        ),
        accordion_section(
            f"4. Barreras para el aprendizaje ({PiarState.barreras.length()})",
            "barreras",
            multi_entry_section("barreras", PiarState.barreras),
        ),
        accordion_section(
            f"5. Ajustes razonables ({PiarState.ajustes.length()})",
            "ajustes",
            multi_entry_section("ajustes", PiarState.ajustes),
        ),
        accordion_section(
            f"6. Estrategias pedagógicas ({PiarState.estrategias.length()})",
            "estrategias",
            multi_entry_section("estrategias", PiarState.estrategias),
        ),
        accordion_section(
            f"7. Seguimiento y evaluación ({PiarState.seguimiento.length()})",
            "seguimiento",
            multi_entry_section("seguimiento", PiarState.seguimiento),
        ),
        accordion_section(
            "8. Acta de acuerdos y compromisos",
            "acta_acuerdos",
            single_entry_section(
                "acta_acuerdos",
                {
                    "acuerdos": {
                        "label": "Acuerdos",
                        "placeholder": "Acuerdos entre la institución, la familia y el estudiante...",
                    },
                    "compromisos": {
                        "label": "Compromisos",
                        "placeholder": "Compromisos de cada una de las partes...",
                    },
                },
            ),
        ),
        class_name="w-full max-w-6xl mx-auto pb-12",
    )