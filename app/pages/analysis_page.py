import reflex as rx
from app.states.analysis_state import AnalysisState


def metric_card(title: str, chart: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-semibold text-neutral-800 mb-4"),
        chart,
        class_name="p-6 bg-white border border-neutral-200 rounded-xl shadow-sm",
    )


def analysis_page() -> rx.Component:
    """Página de análisis grupal y por grado."""
    return rx.el.div(
        rx.el.h1("Análisis Grupal", class_name="text-3xl font-bold text-neutral-800"),
        rx.el.p(
            "Visualice métricas y tendencias de los PIARs por grado y sede.",
            class_name="text-neutral-600 mt-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label("Filtrar por Grado", class_name="text-sm font-medium"),
                rx.el.select(
                    rx.foreach(
                        AnalysisState.grades, lambda g: rx.el.option(g, value=g)
                    ),
                    on_change=AnalysisState.set_selected_grade,
                    default_value="",
                    class_name="w-full mt-1 p-2 border rounded-md",
                ),
            ),
            rx.el.div(
                rx.el.label("Filtrar por Sede", class_name="text-sm font-medium"),
                rx.el.select(
                    rx.foreach(AnalysisState.sedes, lambda s: rx.el.option(s, value=s)),
                    on_change=AnalysisState.set_selected_sede,
                    default_value="",
                    class_name="w-full mt-1 p-2 border rounded-md",
                ),
            ),
            class_name="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
        ),
        rx.el.div(
            metric_card(
                "Tipos de Barreras Identificadas",
                rx.recharts.pie_chart(
                    rx.recharts.pie(
                        data=AnalysisState.barrier_types_data,
                        data_key="value",
                        name_key="name",
                        cx="50%",
                        cy="50%",
                        outer_radius=80,
                        fill="#8884d8",
                        label=True,
                    ),
                    rx.recharts.tooltip(),
                    height=300,
                ),
            ),
            metric_card(
                "Ajustes Razonables Frecuentes",
                rx.recharts.bar_chart(
                    rx.recharts.bar(data_key="value", fill="#82ca9d"),
                    rx.recharts.x_axis(data_key="name"),
                    rx.recharts.y_axis(),
                    rx.recharts.tooltip(),
                    data=AnalysisState.frequent_adjustments_data,
                    height=300,
                ),
            ),
            metric_card(
                "Estado General de PIARs",
                rx.recharts.pie_chart(
                    rx.recharts.pie(
                        data=AnalysisState.piar_status_data,
                        data_key="value",
                        name_key="name",
                        cx="50%",
                        cy="50%",
                        inner_radius=60,
                        outer_radius=80,
                        padding_angle=5,
                        fill="#ffc658",
                        label=True,
                    ),
                    rx.recharts.tooltip(),
                    height=300,
                ),
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="w-full",
    )