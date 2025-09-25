import reflex as rx


class AnalysisState(rx.State):
    """State for the group analysis dashboard."""

    selected_grade: str = ""
    selected_sede: str = ""
    grades: list[str] = [
        "Todos",
        "1er Grado",
        "2do Grado",
        "3er Grado",
        "4to Grado",
        "5to Grado",
    ]
    sedes: list[str] = ["Todas", "Sede Principal", "Sede Anexa"]
    barrier_types_data: list[dict] = [
        {"name": "Actitudinal", "value": 40},
        {"name": "Curricular", "value": 30},
        {"name": "Física", "value": 20},
        {"name": "Comunicativa", "value": 10},
    ]
    frequent_adjustments_data: list[dict] = [
        {"name": "Tiempo de evaluación", "value": 50},
        {"name": "Materiales adaptados", "value": 45},
        {"name": "Apoyos humanos", "value": 25},
        {"name": "Evaluación diferenciada", "value": 15},
    ]
    piar_status_data: list[dict] = [
        {"name": "Completado", "value": 60},
        {"name": "En Progreso", "value": 30},
        {"name": "Pendiente", "value": 10},
    ]

    @rx.event
    def set_selected_grade(self, grade: str):
        self.selected_grade = grade

    @rx.event
    def set_selected_sede(self, sede: str):
        self.selected_sede = sede