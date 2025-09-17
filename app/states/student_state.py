import reflex as rx
from typing import TypedDict, Literal


class Student(TypedDict):
    id: int
    name: str
    grade: str
    status: str
    avatar: str


TabName = Literal[
    "Identificación del estudiante",
    "Información académica",
    "Información familiar",
    "Información de salud",
    "Aspectos pedagógicos iniciales",
]


class StudentState(rx.State):
    """State for the students page."""

    students: list[Student] = [
        {
            "id": 1,
            "name": "Ana García",
            "grade": "3er Grado",
            "status": "Activo",
            "avatar": "Ana Garcia",
        },
        {
            "id": 2,
            "name": "Luis Pérez",
            "grade": "5to Grado",
            "status": "Activo",
            "avatar": "Luis Perez",
        },
        {
            "id": 3,
            "name": "Sofía Rodriguez",
            "grade": "1er Grado",
            "status": "Inactivo",
            "avatar": "Sofia Rodriguez",
        },
        {
            "id": 4,
            "name": "Carlos Martinez",
            "grade": "3er Grado",
            "status": "Activo",
            "avatar": "Carlos Martinez",
        },
        {
            "id": 5,
            "name": "Maria Hernandez",
            "grade": "2do Grado",
            "status": "Activo",
            "avatar": "Maria Hernandez",
        },
    ]
    show_add_student_modal: bool = False
    active_tab: TabName = "Identificación del estudiante"

    @rx.event
    def toggle_add_student_modal(self):
        """Toggles the add student modal visibility."""
        self.show_add_student_modal = not self.show_add_student_modal
        if self.show_add_student_modal:
            self.active_tab = "Identificación del estudiante"

    @rx.event
    def set_active_tab(self, tab_name: TabName):
        """Sets the active tab in the modal."""
        self.active_tab = tab_name

    @rx.event
    def add_student(self, form_data: dict):
        """Adds a new student from the form data."""
        if not all(
            (form_data.get(field) for field in ["nombres", "apellidos", "grado_actual"])
        ):
            return rx.toast.error("Por favor complete todos los campos requeridos.")
        new_id = max((s["id"] for s in self.students), default=0) + 1
        new_name = (
            f"{form_data.get('nombres', '')} {form_data.get('apellidos', '')}".strip()
        )
        new_student: Student = {
            "id": new_id,
            "name": new_name,
            "grade": form_data.get("grado_actual", "N/A"),
            "status": "Activo",
            "avatar": new_name,
        }
        self.students.append(new_student)
        self.show_add_student_modal = False
        return rx.toast.success(f"Estudiante '{new_name}' añadido exitosamente.")