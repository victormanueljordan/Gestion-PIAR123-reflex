import reflex as rx
from app.states.piar_state import PiarState


def item_modal() -> rx.Component:
    is_interdisciplinar = PiarState.editing_section == "valoracion_interdisciplinar"
    default_item = PiarState.editing_item
    return rx.el.dialog(
        rx.el.div(
            class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
            on_click=PiarState.close_item_modal,
        ),
        rx.el.div(
            rx.el.form(
                rx.el.h2(
                    rx.cond(
                        PiarState.editing_item.is_not_none(),
                        "Editar Registro",
                        "Añadir Nuevo Registro",
                    ),
                    class_name="text-lg font-bold text-neutral-800 p-6 border-b",
                ),
                rx.el.div(
                    rx.cond(
                        ~is_interdisciplinar,
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Materia/Área", class_name="text-sm font-medium"
                                ),
                                rx.el.select(
                                    rx.foreach(
                                        PiarState.materias,
                                        lambda m: rx.el.option(m, value=m),
                                    ),
                                    name="materia",
                                    default_value=default_item["materia"].to(str),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Periodo", class_name="text-sm font-medium"
                                ),
                                rx.el.select(
                                    rx.foreach(
                                        PiarState.periodos,
                                        lambda p: rx.el.option(p, value=p),
                                    ),
                                    name="periodo",
                                    default_value=default_item["periodo"].to(str),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4",
                            ),
                            class_name="grid grid-cols-2 gap-4",
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        is_interdisciplinar,
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Disciplina/Área Profesional",
                                    class_name="text-sm font-medium",
                                ),
                                rx.el.input(
                                    name="disciplina",
                                    default_value=default_item["disciplina"].to(str),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4 col-span-2",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Profesional Responsable",
                                    class_name="text-sm font-medium",
                                ),
                                rx.el.input(
                                    name="profesional_responsable",
                                    default_value=default_item[
                                        "profesional_responsable"
                                    ].to(str),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Fecha de Concepto",
                                    class_name="text-sm font-medium",
                                ),
                                rx.el.input(
                                    name="fecha_concepto",
                                    type_="date",
                                    default_value=default_item["fecha_concepto"].to(
                                        str
                                    ),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Resumen del Concepto",
                                    class_name="text-sm font-medium",
                                ),
                                rx.el.textarea(
                                    name="resumen_concepto",
                                    default_value=default_item["resumen_concepto"].to(
                                        str
                                    ),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    rows=3,
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4 col-span-2",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Recomendaciones", class_name="text-sm font-medium"
                                ),
                                rx.el.textarea(
                                    name="recomendaciones",
                                    default_value=default_item["recomendaciones"].to(
                                        str
                                    ),
                                    class_name="mt-1 w-full p-2 border rounded-md",
                                    rows=3,
                                    disabled=PiarState.is_final,
                                ),
                                class_name="mb-4 col-span-2",
                            ),
                            class_name="grid grid-cols-2 gap-4",
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        PiarState.editing_section == "barreras",
                        rx.el.div(
                            rx.el.label(
                                "Tipo de Barrera", class_name="text-sm font-medium"
                            ),
                            rx.el.select(
                                rx.foreach(
                                    PiarState.tipos_barrera,
                                    lambda t: rx.el.option(t, value=t),
                                ),
                                name="tipo_barrera",
                                default_value=default_item["tipo_barrera"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Descripción de la Barrera",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="descripcion",
                                default_value=default_item["descripcion"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Evidencias/Ejemplos",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="evidencias",
                                default_value=default_item["evidencias"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        PiarState.editing_section == "ajustes",
                        rx.el.div(
                            rx.el.label(
                                "Categoría de Ajuste", class_name="text-sm font-medium"
                            ),
                            rx.el.select(
                                rx.foreach(
                                    PiarState.categorias_ajuste,
                                    lambda c: rx.el.option(c, value=c),
                                ),
                                name="categoria_ajuste",
                                default_value=default_item["categoria_ajuste"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Descripción del Ajuste",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="descripcion",
                                default_value=default_item["descripcion"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Recursos Requeridos",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="recursos_requeridos",
                                default_value=default_item["recursos_requeridos"].to(
                                    str
                                ),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        PiarState.editing_section == "estrategias",
                        rx.el.div(
                            rx.el.label(
                                "Método Sugerido", class_name="text-sm font-medium"
                            ),
                            rx.el.input(
                                name="metodo_sugerido",
                                default_value=default_item["metodo_sugerido"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Descripción de la Estrategia",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="descripcion",
                                default_value=default_item["descripcion"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        PiarState.editing_section == "seguimiento",
                        rx.el.div(
                            rx.el.label(
                                "Observaciones del Avance",
                                class_name="text-sm font-medium",
                            ),
                            rx.el.textarea(
                                name="observaciones_avance",
                                default_value=default_item["observaciones_avance"].to(
                                    str
                                ),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Evidencias Recolectadas",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="evidencias_recolectadas",
                                default_value=default_item[
                                    "evidencias_recolectadas"
                                ].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                            rx.el.label(
                                "Acciones de Mejora o Próximos Pasos",
                                class_name="text-sm font-medium mt-4",
                            ),
                            rx.el.textarea(
                                name="acciones_mejora",
                                default_value=default_item["acciones_mejora"].to(str),
                                class_name="mt-1 w-full p-2 border rounded-md",
                                rows=3,
                                disabled=PiarState.is_final,
                            ),
                        ),
                        rx.fragment(),
                    ),
                    class_name="p-6 h-96 overflow-y-auto",
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
                        disabled=PiarState.is_final,
                    ),
                    class_name="flex justify-end gap-4 p-6 border-t",
                ),
                on_submit=PiarState.save_item,
                reset_on_submit=True,
            ),
            class_name="bg-white rounded-xl shadow-2xl w-full max-w-2xl flex flex-col z-50",
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
            rows=4,
            disabled=PiarState.is_final,
            default_value=value,
        ),
        class_name="mb-4",
    )


def single_entry_section(section_name: str, fields: list[dict]) -> rx.Component:
    return rx.el.div(
        rx.foreach(
            fields,
            lambda field: text_area_field(
                field["label"],
                field["placeholder"],
                PiarState.caracterizacion[field["name"]],
                lambda val: PiarState.update_single_entry_field(
                    section_name, field["name"], val
                ),
            ),
        )
    )


def multi_entry_section(
    section_key: str, items: rx.Var[list], columns: list[str]
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.foreach(
                            columns + ["Acciones"],
                            lambda col: rx.el.th(
                                col,
                                class_name="px-4 py-2 text-left text-sm font-semibold text-neutral-600 bg-neutral-50",
                            ),
                        )
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        items,
                        lambda item: rx.el.tr(
                            rx.foreach(
                                columns,
                                lambda col_key: rx.el.td(
                                    item[
                                        col_key.lower()
                                        .replace(" ", "_")
                                        .replace("/", "_")
                                    ],
                                    class_name="px-4 py-2 border-t max-w-xs truncate",
                                ),
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
        rx.cond(is_open, rx.el.div(content, class_name="p-6 bg-white"), rx.fragment()),
        class_name="border border-neutral-200 rounded-lg shadow-sm mb-4",
    )


def valoracion_pedagogica_section() -> rx.Component:
    areas = [
        ("lectoescritura", "Lectoescritura"),
        ("matematicas", "Matemáticas"),
        ("ciencias_naturales", "Ciencias Naturales"),
        ("ciencias_sociales", "Ciencias Sociales"),
        ("otras_areas", "Otras Áreas (Arte, Ed. Física, etc)"),
    ]
    return rx.el.div(
        rx.foreach(
            areas,
            lambda area: rx.el.div(
                rx.el.h3(
                    area[1], class_name="font-semibold text-md text-neutral-700 mb-2"
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label("Nivel", class_name="text-sm font-medium"),
                        rx.el.select(
                            rx.foreach(
                                PiarState.niveles_desempeno,
                                lambda n: rx.el.option(n, value=n),
                            ),
                            default_value=PiarState.valoracion_pedagogica[area[0]][
                                "nivel"
                            ],
                            on_change=lambda val: PiarState.update_valoracion_pedagogica_field(
                                area[0], "nivel", val
                            ),
                            class_name="mt-1 w-full p-2 border rounded-md",
                            disabled=PiarState.is_final,
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.el.label("Observaciones", class_name="text-sm font-medium"),
                        rx.el.textarea(
                            default_value=PiarState.valoracion_pedagogica[area[0]][
                                "observaciones"
                            ],
                            on_change=lambda val: PiarState.update_valoracion_pedagogica_field(
                                area[0], "observaciones", val
                            ),
                            class_name="mt-1 w-full p-2 border rounded-md",
                            rows=3,
                            disabled=PiarState.is_final,
                        ),
                        class_name="flex-1",
                    ),
                    class_name="grid md:grid-cols-2 gap-4",
                ),
                class_name="mb-6 p-4 border rounded-md bg-neutral-50",
            ),
        ),
        text_area_field(
            "Observaciones Generales",
            "Resumen del desempeño global del estudiante...",
            PiarState.valoracion_observaciones_generales,
            PiarState.set_valoracion_observaciones_generales,
        ),
    )


def acta_acuerdos_section() -> rx.Component:
    fields = [
        ("compromisos_institucion", "Compromisos de la institución educativa"),
        ("compromisos_familia", "Compromisos de la familia"),
        ("compromisos_estudiante", "Compromisos del estudiante"),
        ("compromisos_apoyos_externos", "Compromisos de apoyos externos"),
        ("firmas", "Firmas (docente, acudiente, etc.)"),
    ]
    return rx.el.div(
        rx.foreach(
            fields,
            lambda f: text_area_field(
                f[1],
                f"Describa los {f[1].lower()}...",
                PiarState.acta_acuerdos[f[0]],
                lambda val: PiarState.update_single_entry_field(
                    "acta_acuerdos", f[0], val
                ),
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Fecha de Firma",
                class_name="block text-sm font-medium text-neutral-700 mb-1",
            ),
            rx.el.input(
                type_="date",
                default_value=PiarState.acta_acuerdos["fecha_firma"],
                on_change=lambda val: PiarState.update_single_entry_field(
                    "acta_acuerdos", "fecha_firma", val
                ),
                class_name="w-full md:w-1/3 p-2 border rounded-md",
                disabled=PiarState.is_final,
            ),
        ),
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
                [
                    {
                        "name": "estilo_ritmo_aprendizaje",
                        "label": "Estilo y ritmo de aprendizaje",
                        "placeholder": "Describa cómo aprende mejor el estudiante...",
                    },
                    {
                        "name": "fortalezas",
                        "label": "Fortalezas",
                        "placeholder": "Habilidades, talentos y puntos fuertes...",
                    },
                    {
                        "name": "intereses",
                        "label": "Intereses",
                        "placeholder": "Gustos, motivaciones y temas de interés...",
                    },
                    {
                        "name": "necesidades_especiales",
                        "label": "Necesidades educativas especiales identificadas",
                        "placeholder": "Diagnósticos, barreras específicas...",
                    },
                    {
                        "name": "contexto_familiar_social",
                        "label": "Contexto familiar/social relevante",
                        "placeholder": "Aspectos del entorno que influyen en el aprendizaje...",
                    },
                ],
            ),
        ),
        accordion_section(
            "2. Valoración pedagógica",
            "valoracion_pedagogica",
            valoracion_pedagogica_section(),
        ),
        accordion_section(
            f"3. Valoración interdisciplinar ({PiarState.valoracion_interdisciplinar.length()})",
            "valoracion_interdisciplinar",
            multi_entry_section(
                "valoracion_interdisciplinar",
                PiarState.valoracion_interdisciplinar,
                ["Disciplina", "Profesional Responsable", "Fecha Concepto"],
            ),
        ),
        accordion_section(
            f"4. Estrategias pedagógicas ({PiarState.estrategias.length()})",
            "estrategias",
            multi_entry_section(
                "estrategias",
                PiarState.estrategias,
                ["Materia", "Periodo", "Método Sugerido"],
            ),
        ),
        accordion_section(
            f"5. Seguimiento y evaluación ({PiarState.seguimiento.length()})",
            "seguimiento",
            multi_entry_section(
                "seguimiento",
                PiarState.seguimiento,
                ["Materia", "Periodo", "Observaciones Avance"],
            ),
        ),
        accordion_section(
            "6. Acta de acuerdos y compromisos",
            "acta_acuerdos",
            acta_acuerdos_section(),
        ),
        class_name="w-full max-w-6xl mx-auto pb-12",
    )