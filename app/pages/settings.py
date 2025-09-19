import reflex as rx
from app.states.settings_state import (
    SettingsState,
    Sede,
    Periodo,
    CatalogoItem,
    Grado,
    Area,
)


def accordion_item(title: str, content: rx.Component, section_key: str) -> rx.Component:
    is_open = SettingsState.active_accordion == section_key
    return rx.el.div(
        rx.el.button(
            rx.el.div(
                rx.el.h3(title, class_name="text-lg font-semibold text-neutral-800"),
                rx.icon(
                    tag=rx.cond(is_open, "chevron-down", "chevron-right"),
                    class_name="h-5 w-5 text-neutral-500",
                ),
                class_name="flex justify-between items-center w-full",
            ),
            on_click=lambda: SettingsState.set_active_accordion(section_key),
            class_name="w-full text-left p-4 bg-neutral-100 rounded-t-lg",
        ),
        rx.cond(is_open, rx.el.div(content, class_name="p-6 bg-white"), rx.el.div()),
        class_name="border border-neutral-200 rounded-lg shadow-sm mb-4",
    )


def form_input(
    label: str,
    name: str,
    value: rx.Var,
    on_change,
    placeholder: str = "",
    type: str = "text",
    required: bool = False,
    disabled: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            rx.cond(required, rx.el.span(" *", class_name="text-red-500"), ""),
            class_name="block text-sm font-medium text-neutral-700 mb-1",
        ),
        rx.el.input(
            name=name,
            default_value=value,
            on_change=on_change,
            placeholder=placeholder,
            type=type,
            required=required,
            disabled=disabled,
            class_name="w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 disabled:bg-neutral-50",
        ),
        class_name="w-full",
    )


def form_select(
    label: str,
    name: str,
    value: rx.Var,
    on_change,
    options: list[str],
    required: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            rx.cond(required, rx.el.span(" *", class_name="text-red-500"), ""),
            class_name="block text-sm font-medium text-neutral-700 mb-1",
        ),
        rx.el.select(
            rx.foreach(options, lambda opt: rx.el.option(opt, value=opt)),
            name=name,
            default_value=value,
            on_change=on_change,
            required=required,
            class_name="w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
        ),
        class_name="w-full",
    )


def form_multiselect(
    label: str, name: str, values: rx.Var[list[str]], on_change, options: list[str]
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-sm font-medium text-neutral-700 mb-2"
        ),
        rx.el.div(
            rx.foreach(
                options,
                lambda opt: rx.el.div(
                    rx.el.input(
                        type="checkbox",
                        name=f"{name}_{opt}",
                        is_checked=values.contains(opt),
                        on_change=lambda _: on_change(name, opt),
                        class_name="h-4 w-4 text-indigo-600 border-neutral-300 rounded focus:ring-indigo-500",
                    ),
                    rx.el.label(opt, class_name="ml-2 text-sm text-neutral-600"),
                    class_name="flex items-center",
                ),
            ),
            class_name="grid grid-cols-2 md:grid-cols-3 gap-2",
        ),
    )


def datos_institucion_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            form_input(
                "Nombre oficial",
                "nombre_oficial",
                SettingsState.institucion["nombre_oficial"],
                lambda v: SettingsState.update_institucion_field("nombre_oficial", v),
                required=True,
            ),
            form_input(
                "Código DANE / NIT",
                "codigo_dane",
                SettingsState.institucion["codigo_dane"],
                lambda v: SettingsState.update_institucion_field("codigo_dane", v),
            ),
            class_name="grid md:grid-cols-2 gap-6 mb-6",
        ),
        rx.el.div(
            form_select(
                "Naturaleza",
                "naturaleza",
                SettingsState.institucion["naturaleza"],
                lambda v: SettingsState.update_institucion_field("naturaleza", v),
                ["Pública", "Privada"],
                required=True,
            ),
            form_select(
                "Calendario",
                "calendario",
                SettingsState.institucion["calendario"],
                lambda v: SettingsState.update_institucion_field("calendario", v),
                ["A", "B"],
                required=True,
            ),
            class_name="grid md:grid-cols-2 gap-6 mb-6",
        ),
        rx.el.div(
            form_multiselect(
                "Niveles",
                "niveles",
                SettingsState.institucion["niveles"],
                SettingsState.toggle_institucion_multiselect,
                ["Preescolar", "Básica", "Media"],
            ),
            form_multiselect(
                "Jornadas disponibles",
                "jornadas",
                SettingsState.institucion["jornadas"],
                SettingsState.toggle_institucion_multiselect,
                ["Mañana", "Tarde", "Única"],
            ),
            class_name="grid md:grid-cols-2 gap-6 mb-6",
        ),
        rx.el.div(
            rx.el.h4(
                "Rector/Director",
                class_name="text-md font-semibold text-neutral-700 mb-2 border-b pb-2",
            ),
            rx.el.div(
                form_input(
                    "Nombre",
                    "rector_nombre",
                    SettingsState.institucion["rector_nombre"],
                    lambda v: SettingsState.update_institucion_field(
                        "rector_nombre", v
                    ),
                ),
                form_input(
                    "Email",
                    "rector_email",
                    SettingsState.institucion["rector_email"],
                    lambda v: SettingsState.update_institucion_field("rector_email", v),
                    type="email",
                ),
                form_input(
                    "Teléfono",
                    "rector_telefono",
                    SettingsState.institucion["rector_telefono"],
                    lambda v: SettingsState.update_institucion_field(
                        "rector_telefono", v
                    ),
                    type="tel",
                ),
                class_name="grid md:grid-cols-3 gap-6",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.h4(
                "Identidad Visual",
                class_name="text-md font-semibold text-neutral-700 mb-2 border-b pb-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Logo",
                        class_name="block text-sm font-medium text-neutral-700 mb-1",
                    ),
                    rx.upload.root(
                        rx.el.div(
                            rx.image(
                                src=SettingsState.logo_url,
                                class_name="h-20 w-20 object-contain rounded-md bg-neutral-100 p-1",
                            ),
                            rx.el.div(
                                rx.el.p("Arrastra y suelta o haz clic para subir"),
                                rx.el.p(
                                    "PNG, JPG (MAX. 800x400px)",
                                    class_name="text-xs text-neutral-500",
                                ),
                                class_name="text-center",
                            ),
                            class_name="flex items-center gap-4 p-4 border-2 border-dashed rounded-lg cursor-pointer",
                        ),
                        id="logo_upload",
                        multiple=False,
                        accept={"image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"]},
                    ),
                    rx.el.button(
                        "Subir Logo",
                        on_click=SettingsState.handle_logo_upload(
                            rx.upload_files(upload_id="logo_upload")
                        ),
                        class_name="mt-2 px-3 py-1 bg-indigo-50 text-indigo-600 text-sm font-semibold rounded-md hover:bg-indigo-100",
                    ),
                    class_name="w-full",
                ),
                rx.el.div(
                    form_input(
                        "Color Primario",
                        "color_primario",
                        SettingsState.institucion["color_primario"],
                        lambda v: SettingsState.update_institucion_field(
                            "color_primario", v
                        ),
                        type="color",
                    ),
                    form_input(
                        "Color Secundario",
                        "color_secundario",
                        SettingsState.institucion["color_secundario"],
                        lambda v: SettingsState.update_institucion_field(
                            "color_secundario", v
                        ),
                        type="color",
                    ),
                    class_name="flex gap-6",
                ),
                class_name="grid md:grid-cols-2 gap-6",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.h4(
                "Sedes",
                class_name="text-md font-semibold text-neutral-700 mb-2 border-b pb-2",
            ),
            rx.foreach(SettingsState.sedes, sede_form_item),
            rx.el.button(
                rx.icon(tag="plus", class_name="mr-2 h-4 w-4"),
                "Añadir Sede",
                on_click=SettingsState.add_sede,
                class_name="mt-4 flex items-center px-4 py-2 bg-neutral-100 text-neutral-700 font-semibold rounded-lg text-sm hover:bg-neutral-200",
            ),
        ),
    )


def sede_form_item(sede: Sede) -> rx.Component:
    sede_id = sede["id"]
    return rx.el.div(
        rx.el.div(
            rx.el.h5(f"Sede: {sede['nombre']}", class_name="font-semibold"),
            rx.el.button(
                rx.icon(tag="trash-2", class_name="h-4 w-4 text-red-500"),
                on_click=lambda: SettingsState.delete_sede(sede_id),
                class_name="p-1 rounded-md hover:bg-red-100",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.el.div(
            form_input(
                "Nombre Sede",
                "nombre",
                sede["nombre"],
                lambda v: SettingsState.update_sede(sede_id, "nombre", v),
            ),
            form_input(
                "Dirección",
                "direccion",
                sede["direccion"],
                lambda v: SettingsState.update_sede(sede_id, "direccion", v),
            ),
            form_input(
                "Ciudad",
                "ciudad",
                sede["ciudad"],
                lambda v: SettingsState.update_sede(sede_id, "ciudad", v),
            ),
            form_input(
                "Teléfono",
                "telefono",
                sede["telefono"],
                lambda v: SettingsState.update_sede(sede_id, "telefono", v),
            ),
            form_input(
                "Email",
                "email",
                sede["email"],
                lambda v: SettingsState.update_sede(sede_id, "email", v),
                type="email",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
        ),
        class_name="p-4 border rounded-md mb-4 bg-neutral-50",
    )


def ano_lectivo_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            form_input(
                "Año lectivo activo",
                "ano_activo",
                SettingsState.ano_lectivo["ano_activo"],
                lambda v: SettingsState.update_ano_lectivo_field("ano_activo", v),
                type="number",
                required=True,
            ),
            form_input(
                "Fecha inicio de clases",
                "fecha_inicio",
                SettingsState.ano_lectivo["fecha_inicio"],
                lambda v: SettingsState.update_ano_lectivo_field("fecha_inicio", v),
                type="date",
            ),
            form_input(
                "Fecha fin de clases",
                "fecha_fin",
                SettingsState.ano_lectivo["fecha_fin"],
                lambda v: SettingsState.update_ano_lectivo_field("fecha_fin", v),
                type="date",
            ),
            class_name="grid md:grid-cols-3 gap-6 mb-6",
        ),
        rx.el.div(
            form_select(
                "Esquema de periodos",
                "esquema_periodos",
                SettingsState.ano_lectivo["esquema_periodos"],
                lambda v: SettingsState.update_ano_lectivo_field("esquema_periodos", v),
                ["Bimestres", "Trimestres", "Semestres"],
                required=True,
            ),
            form_input(
                "Fecha límite de edición PIAR",
                "fecha_limite_cierre",
                SettingsState.ano_lectivo["fecha_limite_cierre"],
                lambda v: SettingsState.update_ano_lectivo_field(
                    "fecha_limite_cierre", v
                ),
                type="date",
            ),
            class_name="grid md:grid-cols-2 gap-6 mb-6",
        ),
        rx.el.div(
            rx.el.h4(
                "Periodos",
                class_name="text-md font-semibold text-neutral-700 mb-2 border-b pb-2",
            ),
            rx.foreach(SettingsState.periodos, periodo_form_item),
            rx.el.button(
                rx.icon(tag="plus", class_name="mr-2 h-4 w-4"),
                "Añadir Periodo",
                on_click=SettingsState.add_periodo,
                class_name="mt-4 flex items-center px-4 py-2 bg-neutral-100 text-neutral-700 font-semibold rounded-lg text-sm hover:bg-neutral-200",
            ),
        ),
    )


def periodo_form_item(periodo: Periodo) -> rx.Component:
    periodo_id = periodo["id"]
    return rx.el.div(
        rx.el.div(
            form_input(
                "Nombre Periodo",
                "nombre",
                periodo["nombre"],
                lambda v: SettingsState.update_periodo(periodo_id, "nombre", v),
            ),
            form_input(
                "Fecha Inicio",
                "fecha_inicio",
                periodo["fecha_inicio"],
                lambda v: SettingsState.update_periodo(periodo_id, "fecha_inicio", v),
                type="date",
            ),
            form_input(
                "Fecha Fin",
                "fecha_fin",
                periodo["fecha_fin"],
                lambda v: SettingsState.update_periodo(periodo_id, "fecha_fin", v),
                type="date",
            ),
            rx.el.div(
                rx.el.label(
                    "¿Activo?",
                    class_name="block text-sm font-medium text-neutral-700 mb-1",
                ),
                rx.el.input(
                    type="checkbox",
                    is_checked=periodo["activo"],
                    on_change=lambda v: SettingsState.update_periodo(
                        periodo_id, "activo", v
                    ),
                    class_name="h-5 w-5 mt-2 text-indigo-600 border-neutral-300 rounded focus:ring-indigo-500",
                ),
                class_name="flex flex-col items-center justify-center",
            ),
            rx.el.button(
                rx.icon(tag="trash-2", class_name="h-4 w-4 text-red-500"),
                on_click=lambda: SettingsState.delete_periodo(periodo_id),
                class_name="p-2 rounded-md hover:bg-red-100 self-end",
            ),
            class_name="grid grid-cols-5 gap-4 items-center",
        ),
        class_name="p-4 border rounded-md mb-4 bg-neutral-50",
    )


def crud_catalogo_section(
    title: str, items: rx.Var[list[CatalogoItem]], catalogo_name: str
) -> rx.Component:
    return rx.el.div(
        rx.el.h4(title, class_name="text-md font-semibold text-neutral-700 mb-2"),
        rx.el.div(
            rx.foreach(
                items,
                lambda item: rx.el.div(
                    rx.el.p(item["nombre"], class_name="flex-grow"),
                    rx.el.button(
                        rx.icon(tag="trash-2", size=16, class_name="text-red-500"),
                        on_click=lambda: SettingsState.delete_catalogo_item(
                            catalogo_name, item["id"]
                        ),
                        class_name="p-1 rounded hover:bg-red-100",
                    ),
                    class_name="flex justify-between items-center p-2 border-b",
                ),
            ),
            class_name="mb-4 max-h-48 overflow-y-auto border rounded-md p-2 bg-neutral-50",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.input(
                    name="nombre",
                    placeholder="Nuevo elemento...",
                    class_name="flex-grow px-3 py-2 bg-white border border-neutral-300 rounded-l-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                rx.el.button(
                    "Añadir",
                    type="submit",
                    class_name="px-4 py-2 bg-indigo-500 text-white font-semibold rounded-r-md text-sm hover:bg-indigo-600",
                ),
                class_name="flex",
            ),
            on_submit=lambda form_data: SettingsState.add_catalogo_item(
                catalogo_name, form_data
            ),
            reset_on_submit=True,
        ),
        class_name="mb-6",
    )


def catalogos_content() -> rx.Component:
    return rx.el.div(
        crud_catalogo_section(
            "Tipos de barrera",
            SettingsState.catalogo_tipos_barrera,
            "catalogo_tipos_barrera",
        ),
        crud_catalogo_section(
            "Categorías de ajustes razonables",
            SettingsState.catalogo_categorias_ajuste,
            "catalogo_categorias_ajuste",
        ),
        crud_catalogo_section(
            "Métodos/Estrategias pedagógicas",
            SettingsState.catalogo_metodos,
            "catalogo_metodos",
        ),
        crud_catalogo_section(
            "Tipos de evidencia",
            SettingsState.catalogo_tipos_evidencia,
            "catalogo_tipos_evidencia",
        ),
        class_name="grid md:grid-cols-2 gap-8",
    )


def grados_cursos_grupos_content() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            SettingsState.grados,
            lambda grado: rx.el.div(
                rx.el.div(
                    rx.el.input(
                        default_value=grado["nombre"],
                        on_blur=lambda val: SettingsState.update_grado_nombre(
                            grado["id"], val
                        ),
                        class_name="flex-grow px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm font-semibold",
                    ),
                    rx.el.button(
                        rx.icon(tag="trash-2", class_name="h-4 w-4 text-red-500"),
                        on_click=lambda: SettingsState.delete_grado(grado["id"]),
                        class_name="p-2 rounded-md hover:bg-red-100",
                    ),
                    class_name="flex items-center gap-2 mb-2",
                ),
                rx.el.div(
                    rx.foreach(
                        grado["grupos"],
                        lambda grupo: rx.el.div(
                            rx.el.input(
                                default_value=grupo["nombre"],
                                on_blur=lambda val: SettingsState.update_grupo_nombre(
                                    grado["id"], grupo["id"], val
                                ),
                                class_name="flex-grow px-2 py-1 bg-white border border-neutral-200 rounded-md text-sm",
                            ),
                            rx.el.button(
                                rx.icon(tag="trash-2", class_name="h-3 w-3"),
                                on_click=lambda: SettingsState.delete_grupo(
                                    grado["id"], grupo["id"]
                                ),
                                class_name="p-1 rounded-md hover:bg-neutral-200 text-neutral-500",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                    ),
                    rx.el.button(
                        "Añadir Grupo",
                        on_click=lambda: SettingsState.add_grupo(grado["id"]),
                        class_name="mt-2 px-2 py-1 bg-indigo-50 text-indigo-600 text-xs font-semibold rounded-md hover:bg-indigo-100",
                    ),
                    class_name="ml-8 pl-4 border-l-2",
                ),
                class_name="p-4 border rounded-md mb-4 bg-neutral-50",
            ),
        ),
        rx.el.button(
            rx.icon(tag="plus", class_name="mr-2 h-4 w-4"),
            "Añadir Grado",
            on_click=SettingsState.add_grado,
            class_name="mt-4 flex items-center px-4 py-2 bg-neutral-100 text-neutral-700 font-semibold rounded-lg text-sm hover:bg-neutral-200",
        ),
    )


def areas_asignaturas_content() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            SettingsState.areas,
            lambda area: rx.el.div(
                rx.el.div(
                    rx.el.input(
                        default_value=area["nombre"],
                        on_blur=lambda val: SettingsState.update_area_nombre(
                            area["id"], val
                        ),
                        class_name="flex-grow px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm font-semibold",
                    ),
                    rx.el.button(
                        rx.icon(tag="trash-2", class_name="h-4 w-4 text-red-500"),
                        on_click=lambda: SettingsState.delete_area(area["id"]),
                        class_name="p-2 rounded-md hover:bg-red-100",
                    ),
                    class_name="flex items-center gap-2 mb-2",
                ),
                rx.el.div(
                    rx.foreach(
                        area["asignaturas"],
                        lambda asignatura: rx.el.div(
                            rx.el.input(
                                default_value=asignatura["nombre"],
                                on_blur=lambda val: SettingsState.update_asignatura_nombre(
                                    area["id"], asignatura["id"], val
                                ),
                                class_name="flex-grow px-2 py-1 bg-white border border-neutral-200 rounded-md text-sm",
                            ),
                            rx.el.button(
                                rx.icon(tag="trash-2", class_name="h-3 w-3"),
                                on_click=lambda: SettingsState.delete_asignatura(
                                    area["id"], asignatura["id"]
                                ),
                                class_name="p-1 rounded-md hover:bg-neutral-200 text-neutral-500",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                    ),
                    rx.el.button(
                        "Añadir Asignatura",
                        on_click=lambda: SettingsState.add_asignatura(area["id"]),
                        class_name="mt-2 px-2 py-1 bg-indigo-50 text-indigo-600 text-xs font-semibold rounded-md hover:bg-indigo-100",
                    ),
                    class_name="ml-8 pl-4 border-l-2",
                ),
                class_name="p-4 border rounded-md mb-4 bg-neutral-50",
            ),
        ),
        rx.el.button(
            rx.icon(tag="plus", class_name="mr-2 h-4 w-4"),
            "Añadir Área",
            on_click=SettingsState.add_area,
            class_name="mt-4 flex items-center px-4 py-2 bg-neutral-100 text-neutral-700 font-semibold rounded-lg text-sm hover:bg-neutral-200",
        ),
        class_name="grid md:grid-cols-2 gap-8",
    )


def placeholder_content(title: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f"Contenido para {title} en construcción.", class_name="text-neutral-500"
        )
    )


def settings_page() -> rx.Component:
    """Page for adjusting app and profile settings."""
    return rx.el.div(
        rx.el.h1("Configuración", class_name="text-3xl font-bold text-neutral-800"),
        rx.el.p(
            "Ajusta todos los parámetros de la institución y del sistema.",
            class_name="text-neutral-600 mt-1 mb-8",
        ),
        accordion_item(
            "1. Datos de la institución", datos_institucion_content(), "institucion"
        ),
        accordion_item(
            "2. Año lectivo y periodos", ano_lectivo_content(), "ano_lectivo"
        ),
        accordion_item(
            "3. Grados, cursos y grupos", grados_cursos_grupos_content(), "grados"
        ),
        accordion_item("4. Áreas y asignaturas", areas_asignaturas_content(), "areas"),
        accordion_item(
            "5. Docentes y roles", placeholder_content("Docentes"), "docentes"
        ),
        accordion_item(
            "6. Catálogos pedagógicos (PIAR)", catalogos_content(), "catalogos"
        ),
        accordion_item(
            "7. Recursos e infraestructura", placeholder_content("Recursos"), "recursos"
        ),
        accordion_item(
            "8. Parámetros del PIAR y flujos",
            placeholder_content("Parámetros PIAR"),
            "piar_params",
        ),
        accordion_item(
            "9. Asistente pedagógico (chat)",
            placeholder_content("Asistente"),
            "asistente",
        ),
        accordion_item(
            "10. Privacidad e integraciones",
            placeholder_content("Privacidad"),
            "privacidad",
        ),
        class_name="max-w-5xl mx-auto pb-12",
    )