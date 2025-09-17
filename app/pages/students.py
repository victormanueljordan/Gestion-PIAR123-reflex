import reflex as rx
from app.states.student_state import StudentState, Student


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
                    rx.el.tbody(rx.foreach(StudentState.students, student_row)),
                    class_name="min-w-full bg-white",
                ),
                class_name="overflow-hidden border border-neutral-200 rounded-xl",
            ),
            class_name="mt-8",
        ),
        class_name="w-full",
    )