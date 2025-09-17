import reflex as rx


class DashboardState(rx.State):
    """State for the dashboard page."""

    stats: dict[str, str] = {
        "total_estudiantes": "125",
        "piars_activos": "88",
        "pendientes_revision": "12",
    }
    chart_data: list[dict[str, int | str]] = [
        {"name": "Ene", "piars": 30},
        {"name": "Feb", "piars": 40},
        {"name": "Mar", "piars": 45},
        {"name": "Abr", "piars": 50},
        {"name": "May", "piars": 49},
        {"name": "Jun", "piars": 60},
    ]
    recent_activity: list[dict[str, str]] = [
        {
            "user": "Dr. Morales",
            "action": "actualizó el PIAR de",
            "subject": "Ana García",
            "time": "hace 5 minutos",
        },
        {
            "user": "Admin User",
            "action": "agregó un nuevo estudiante",
            "subject": "Carlos Martinez",
            "time": "hace 2 horas",
        },
        {
            "user": "Sra. Diaz",
            "action": "completó la revisión de",
            "subject": "Luis Pérez",
            "time": "hace 1 día",
        },
    ]