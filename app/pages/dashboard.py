import reflex as rx
from app.states.dashboard_state import DashboardState


def stat_card(title: str, value: rx.Var[str], icon: str) -> rx.Component:
    """A card to display a statistic."""
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=icon, class_name="h-6 w-6 text-indigo-500"),
            class_name="p-3 bg-indigo-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium text-neutral-500"),
            rx.el.p(value, class_name="text-3xl font-bold text-neutral-800"),
            class_name="flex flex-col",
        ),
        class_name="flex items-center gap-4 p-6 bg-white border border-neutral-200 rounded-xl shadow-sm",
    )


def recent_activity_item(activity: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=f"https://api.dicebear.com/9.x/initials/svg?seed={activity['user']}",
            class_name="h-10 w-10 rounded-full",
        ),
        rx.el.div(
            rx.el.p(
                rx.el.span(activity["user"], class_name="font-semibold"),
                f" {activity['action']} ",
                rx.el.span(activity["subject"], class_name="font-semibold"),
                class_name="text-sm text-neutral-700",
            ),
            rx.el.p(activity["time"], class_name="text-xs text-neutral-500"),
        ),
        class_name="flex items-center gap-4",
    )


def dashboard_page() -> rx.Component:
    """The dashboard page with stats, charts, and recent activity."""
    return rx.el.div(
        rx.el.h1("Dashboard", class_name="text-3xl font-bold text-neutral-800"),
        rx.el.p(
            "Bienvenido al panel de control de PIAR123.",
            class_name="text-neutral-600 mt-1",
        ),
        rx.el.div(
            stat_card(
                "Total Estudiantes", DashboardState.stats["total_estudiantes"], "users"
            ),
            stat_card(
                "PIARs Activos", DashboardState.stats["piars_activos"], "file-check-2"
            ),
            stat_card(
                "Pendientes de Revisión",
                DashboardState.stats["pendientes_revision"],
                "file-clock",
            ),
            class_name="mt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Progreso de PIARs (Últimos 6 meses)",
                    class_name="text-lg font-semibold text-neutral-800",
                ),
                rx.recharts.bar_chart(
                    rx.recharts.bar(
                        data_key="piars",
                        fill="#6366F1",
                        radius=[4, 4, 0, 0],
                        bar_size=20,
                    ),
                    rx.recharts.x_axis(data_key="name"),
                    rx.recharts.y_axis(),
                    rx.recharts.tooltip(),
                    data=DashboardState.chart_data,
                    height=300,
                ),
                class_name="p-6 bg-white border border-neutral-200 rounded-xl shadow-sm",
            ),
            rx.el.div(
                rx.el.h2(
                    "Actividad Reciente",
                    class_name="text-lg font-semibold text-neutral-800 mb-4",
                ),
                rx.el.div(
                    rx.foreach(DashboardState.recent_activity, recent_activity_item),
                    class_name="flex flex-col gap-4",
                ),
                class_name="p-6 bg-white border border-neutral-200 rounded-xl shadow-sm",
            ),
            class_name="mt-6 grid grid-cols-1 xl:grid-cols-2 gap-6",
        ),
        class_name="w-full",
    )