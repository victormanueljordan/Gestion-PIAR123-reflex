import reflex as rx
from typing import TypedDict, Literal
import math


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
        {
            "id": 6,
            "name": "José González",
            "grade": "5to Grado",
            "status": "Activo",
            "avatar": "Jose Gonzalez",
        },
        {
            "id": 7,
            "name": "Laura López",
            "grade": "1er Grado",
            "status": "Activo",
            "avatar": "Laura Lopez",
        },
    ]
    show_add_student_modal: bool = False
    active_tab: TabName = "Identificación del estudiante"
    form_data: dict[str, str] = {}
    search_query: str = ""
    grade_filter: str = ""
    status_filter: str = ""
    current_page: int = 1
    page_size: int = 5

    @rx.event
    def update_form_field(self, field: str, value: str):
        self.form_data[field] = value

    @rx.var
    def grade_options(self) -> list[str]:
        grades = {student["grade"] for student in self.students}
        return ["Todos los grados"] + sorted(list(grades))

    @rx.var
    def filtered_students(self) -> list[Student]:
        """Returns the filtered list of students."""
        return [
            student
            for student in self.students
            if self.search_query.lower() in student["name"].lower()
            and (not self.grade_filter or student["grade"] == self.grade_filter)
            and (not self.status_filter or student["status"] == self.status_filter)
        ]

    @rx.var
    def total_pages(self) -> int:
        """Returns the total number of pages."""
        if not self.filtered_students:
            return 1
        return math.ceil(len(self.filtered_students) / self.page_size)

    @rx.var
    def paginated_students(self) -> list[Student]:
        """Returns the paginated list of students for the current page."""
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.filtered_students[start:end]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query
        self.current_page = 1

    @rx.event
    def set_grade_filter(self, grade: str):
        self.grade_filter = grade if grade != "Todos los grados" else ""
        self.current_page = 1

    @rx.event
    def set_status_filter(self, status: str):
        self.status_filter = status if status != "Todos los estados" else ""
        self.current_page = 1

    @rx.event
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    @rx.event
    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1

    @rx.event
    def toggle_add_student_modal(self):
        """Toggles the add student modal visibility."""
        self.show_add_student_modal = not self.show_add_student_modal
        if self.show_add_student_modal:
            self.active_tab = "Identificación del estudiante"
            self.form_data = {}

    @rx.event
    def set_active_tab(self, tab_name: TabName):
        """Sets the active tab in the modal."""
        self.active_tab = tab_name

    @rx.event
    def add_student(self, form_data: dict):
        """Adds a new student from the form data."""
        all_form_data = {**self.form_data, **form_data}
        if not all(
            (
                all_form_data.get(field)
                for field in ["nombres", "apellidos", "grado_actual"]
            )
        ):
            return rx.toast.error(
                "Por favor complete los campos requeridos de la pestaña de identificación."
            )
        new_id = max((s["id"] for s in self.students), default=0) + 1
        new_name = f"{all_form_data.get('nombres', '')} {all_form_data.get('apellidos', '')}".strip()
        new_student: Student = {
            "id": new_id,
            "name": new_name,
            "grade": all_form_data.get("grado_actual", "N/A"),
            "status": "Activo",
            "avatar": new_name,
        }
        self.students.append(new_student)
        self.show_add_student_modal = False
        return rx.toast.success(f"Estudiante '{new_name}' añadido exitosamente.")