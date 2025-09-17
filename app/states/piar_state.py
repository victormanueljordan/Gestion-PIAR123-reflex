import reflex as rx
from typing import TypedDict


class PiarFormat(TypedDict):
    id: int
    student_name: str
    creation_date: str
    status: str


class PiarState(rx.State):
    """State for the PIAR formats page."""

    piar_formats: list[PiarFormat] = [
        {
            "id": 101,
            "student_name": "Ana García",
            "creation_date": "2024-05-15",
            "status": "Completado",
        },
        {
            "id": 102,
            "student_name": "Luis Pérez",
            "creation_date": "2024-05-18",
            "status": "En Progreso",
        },
        {
            "id": 103,
            "student_name": "Sofía Rodriguez",
            "creation_date": "2024-05-20",
            "status": "Pendiente",
        },
        {
            "id": 104,
            "student_name": "Carlos Martinez",
            "creation_date": "2024-05-21",
            "status": "En Progreso",
        },
    ]