import reflex as rx
from app.states.student_state import StudentState, TabName


def form_field(
    label: str, name: str, placeholder: str, field_type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-sm font-medium text-neutral-600 mb-1"
        ),
        rx.el.input(
            name=name,
            placeholder=placeholder,
            type_=field_type,
            class_name="w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
        ),
        class_name="col-span-1 md:col-span-1",
    )


def textarea_field(label: str, name: str, placeholder: str) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-sm font-medium text-neutral-600 mb-1"
        ),
        rx.el.textarea(
            name=name,
            placeholder=placeholder,
            class_name="w-full px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
            rows=4,
        ),
        class_name="col-span-1 md:col-span-2",
    )


def tab_button(name: TabName) -> rx.Component:
    return rx.el.button(
        name,
        on_click=lambda: StudentState.set_active_tab(name),
        class_name=rx.cond(
            StudentState.active_tab == name,
            "px-4 py-2 text-sm font-semibold text-indigo-600 border-b-2 border-indigo-600 bg-indigo-50",
            "px-4 py-2 text-sm font-medium text-neutral-500 hover:text-neutral-700 hover:bg-neutral-100",
        ),
        type_="button",
    )


def identification_tab() -> rx.Component:
    return rx.el.div(
        form_field("Nombres", "nombres", "Nombres del estudiante"),
        form_field("Apellidos", "apellidos", "Apellidos del estudiante"),
        form_field("Tipo de Documento", "tipo_documento", "Ej: CC, TI, RC"),
        form_field(
            "Número de Documento", "numero_documento", "Número de identificación"
        ),
        form_field("Fecha de Nacimiento", "fecha_nacimiento", "", "date"),
        form_field("Edad", "edad", "Edad en años", "number"),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
    )


def academic_info_tab() -> rx.Component:
    return rx.el.div(
        form_field("Grado Actual", "grado_actual", "Ej: 5to Grado"),
        form_field(
            "Institución Educativa Anterior",
            "inst_anterior",
            "Nombre de la institución",
        ),
        textarea_field(
            "Historial Académico Relevante",
            "historial_academico",
            "Describa notas, logros o dificultades pasadas.",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
    )


def family_info_tab() -> rx.Component:
    return rx.el.div(
        form_field("Nombre del Acudiente", "nombre_acudiente", "Nombre completo"),
        form_field("Parentesco", "parentesco_acudiente", "Ej: Madre, Padre, Tutor"),
        form_field(
            "Teléfono del Acudiente", "telefono_acudiente", "Número de contacto", "tel"
        ),
        form_field(
            "Email del Acudiente", "email_acudiente", "correo@ejemplo.com", "email"
        ),
        textarea_field(
            "Observaciones Familiares",
            "obs_familiares",
            "Información relevante sobre el entorno familiar.",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
    )


def health_info_tab() -> rx.Component:
    return rx.el.div(
        form_field("EPS", "eps", "Nombre de la Entidad Promotora de Salud"),
        form_field("Tipo de Sangre", "tipo_sangre", "Ej: O+, A-, etc."),
        textarea_field(
            "Alergias Conocidas",
            "alergias",
            "Describa alergias a medicamentos, alimentos, etc.",
        ),
        textarea_field(
            "Condiciones Médicas Relevantes",
            "condiciones_medicas",
            "Diagnósticos, tratamientos actuales, etc.",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
    )


def pedagogical_aspects_tab() -> rx.Component:
    return rx.el.div(
        textarea_field(
            "Fortalezas del Estudiante",
            "fortalezas",
            "Describa las habilidades y talentos del estudiante.",
        ),
        textarea_field(
            "Dificultades de Aprendizaje",
            "dificultades",
            "Describa los desafíos que enfrenta el estudiante.",
        ),
        textarea_field(
            "Intereses y Motivaciones",
            "intereses",
            "¿Qué le gusta y motiva al estudiante?",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
    )


def add_student_modal() -> rx.Component:
    tabs: list[TabName] = [
        "Identificación del estudiante",
        "Información académica",
        "Información familiar",
        "Información de salud",
        "Aspectos pedagógicos iniciales",
    ]
    return rx.el.dialog(
        rx.el.div(
            class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
            on_click=StudentState.toggle_add_student_modal,
        ),
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.el.h2(
                        "Añadir Nuevo Estudiante",
                        class_name="text-xl font-bold text-neutral-800",
                    ),
                    rx.el.button(
                        rx.icon(tag="x", class_name="h-5 w-5"),
                        on_click=StudentState.toggle_add_student_modal,
                        class_name="p-1 rounded-full hover:bg-neutral-200",
                        type_="button",
                    ),
                    class_name="flex justify-between items-center p-6 border-b",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.foreach(tabs, tab_button),
                        class_name="flex border-b overflow-x-auto",
                    ),
                    rx.el.div(
                        rx.match(
                            StudentState.active_tab,
                            ("Identificación del estudiante", identification_tab()),
                            ("Información académica", academic_info_tab()),
                            ("Información familiar", family_info_tab()),
                            ("Información de salud", health_info_tab()),
                            (
                                "Aspectos pedagógicos iniciales",
                                pedagogical_aspects_tab(),
                            ),
                            rx.el.p("Seleccione una pestaña"),
                        ),
                        class_name="p-6 h-96 overflow-y-auto",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancelar",
                        on_click=StudentState.toggle_add_student_modal,
                        class_name="px-4 py-2 bg-neutral-200 text-neutral-800 font-semibold rounded-lg hover:bg-neutral-300 transition-colors",
                        type_="button",
                    ),
                    rx.el.button(
                        "Guardar Estudiante",
                        type="submit",
                        class_name="px-4 py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 transition-colors",
                    ),
                    class_name="flex justify-end gap-4 p-6 border-t",
                ),
                on_submit=StudentState.add_student,
                reset_on_submit=True,
                class_name="bg-white rounded-xl shadow-2xl w-full max-w-4xl flex flex-col",
            ),
            class_name="fixed inset-0 flex items-center justify-center p-4 z-50",
        ),
        open=StudentState.show_add_student_modal,
    )