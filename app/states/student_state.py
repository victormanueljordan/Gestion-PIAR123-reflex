import reflex as rx
from typing import TypedDict


class Student(TypedDict):
    id: int
    name: str
    grade: str
    status: str
    avatar: str


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