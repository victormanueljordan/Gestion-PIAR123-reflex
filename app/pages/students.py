import reflex as rx
from app.states.student_state import StudentState, Student
from app.components.student_form import add_student_modal


def student_actions() -> rx.Component:
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


def student_row(student: Student) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={student['name']}",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.p(
                        student["name"], class_name="font-semibold text-neutral-800"
                    ),
                    rx.el.p(
                        f"ID: {student['id']}", class_name="text-sm text-neutral-500"
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(student["grade"], class_name="px-6 py-4 text-neutral-600"),
        rx.el.td(
            rx.el.span(
                student["status"],
                class_name=rx.cond(
                    student["status"] == "Activo",
                    "px-2 py-1 text-xs font-semibold text-green-800 bg-green-100 rounded-full",
                    "px-2 py-1 text-xs font-semibold text-red-800 bg-red-100 rounded-full",
                ),
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(student_actions(), class_name="px-6 py-4 text-right"),
        class_name="border-b border-neutral-200 hover:bg-neutral-100",
    )


def students_page() -> rx.Component:
    """Page for managing students."""
    return rx.el.div(
        add_student_modal(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Gestión de Estudiantes",
                    class_name="text-3xl font-bold text-neutral-800",
                ),
                rx.el.p(
                    "Administre la información y los ajustes de sus estudiantes.",
                    class_name="text-neutral-600 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("circle_plus", class_name="h-5 w-5"),
                "Añadir Estudiante",
                on_click=StudentState.toggle_add_student_modal,
                class_name="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 transition-colors",
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    placeholder="Buscar por nombre...",
                    on_change=StudentState.set_search_query.debounce(300),
                    class_name="w-full md:w-1/3 px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                rx.el.select(
                    rx.foreach(
                        StudentState.grade_options,
                        lambda grade: rx.el.option(grade, value=grade),
                    ),
                    on_change=StudentState.set_grade_filter,
                    default_value="",
                    class_name="w-full md:w-1/4 px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                rx.el.select(
                    rx.el.option("Todos los estados", value=""),
                    rx.el.option("Activo", value="Activo"),
                    rx.el.option("Inactivo", value="Inactivo"),
                    on_change=StudentState.set_status_filter,
                    default_value="",
                    class_name="w-full md:w-1/4 px-3 py-2 bg-white border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
                class_name="flex flex-col md:flex-row gap-4 mb-6",
            ),
            class_name="mt-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Nombre",
                                class_name="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Grado",
                                class_name="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Estado",
                                class_name="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider",
                            ),
                            rx.el.th("", class_name="px-6 py-3"),
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(StudentState.paginated_students, student_row)
                    ),
                    class_name="min-w-full bg-white",
                ),
                class_name="overflow-hidden border border-neutral-200 rounded-xl",
            ),
            class_name="mt-4",
        ),
        rx.el.div(
            rx.el.p(
                f"Página {StudentState.current_page} de {StudentState.total_pages}",
                class_name="text-sm text-neutral-600",
            ),
            rx.el.div(
                rx.el.button(
                    "Anterior",
                    on_click=StudentState.prev_page,
                    disabled=StudentState.current_page <= 1,
                    class_name="px-4 py-2 text-sm font-semibold bg-white border border-neutral-300 rounded-md shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:cursor-not-allowed",
                ),
                rx.el.button(
                    "Siguiente",
                    on_click=StudentState.next_page,
                    disabled=StudentState.current_page >= StudentState.total_pages,
                    class_name="px-4 py-2 text-sm font-semibold bg-white border border-neutral-300 rounded-md shadow-sm hover:bg-neutral-50 disabled:opacity-50 disabled:cursor-not-allowed",
                ),
                class_name="flex gap-2",
            ),
            class_name="flex justify-between items-center mt-4",
        ),
        class_name="w-full",
    )