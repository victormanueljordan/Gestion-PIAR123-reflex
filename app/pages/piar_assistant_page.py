import reflex as rx
from app.states.piar_state import PiarState


def assistant_chat() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3("Asistente Pedagógico", class_name="font-bold text-white"),
                rx.el.button(
                    rx.icon(tag="x", class_name="h-4 w-4 text-white"),
                    on_click=PiarState.toggle_chat,
                    class_name="p-1 rounded-full hover:bg-white/20",
                ),
                class_name="flex justify-between items-center p-3 bg-indigo-700",
            ),
            rx.el.div(
                rx.foreach(
                    PiarState.chat_messages,
                    lambda msg: rx.el.div(
                        rx.el.p(msg["message"]),
                        class_name=rx.cond(
                            msg["sender"] == "user",
                            "bg-blue-100 p-2 rounded-lg self-end",
                            "bg-gray-200 p-2 rounded-lg self-start",
                        ),
                    ),
                ),
                class_name="flex flex-col gap-2 p-4 h-80 overflow-y-auto",
            ),
            rx.el.div(
                rx.el.input(
                    placeholder="Escribe tu consulta...",
                    class_name="flex-grow p-2 border rounded-l-lg",
                ),
                rx.el.button(
                    "Enviar",
                    class_name="p-2 bg-indigo-600 text-white rounded-r-lg font-semibold",
                ),
                class_name="flex p-3 border-t",
            ),
            class_name="bg-white rounded-lg shadow-2xl flex flex-col w-96",
        ),
        class_name=rx.cond(
            PiarState.show_chat, "fixed bottom-24 right-8 z-50", "hidden"
        ),
    )


def piar_assistant_page() -> rx.Component:
    return rx.el.div(
        assistant_chat(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Asistente PIAR: Barreras y Ajustes",
                    class_name="text-3xl font-bold text-neutral-800",
                ),
                rx.el.p(
                    f"Apoyo para: {PiarState.selected_piar['student_name']}",
                    class_name="text-neutral-600 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("arrow-left", class_name="h-5 w-5"),
                "Volver",
                on_click=PiarState.return_to_piar_list,
                class_name="flex items-center gap-2 px-4 py-2 bg-neutral-200 text-neutral-800 font-semibold rounded-lg hover:bg-neutral-300",
            ),
            class_name="flex items-start justify-between mb-8",
        ),
        rx.el.div(
            rx.el.h2(
                "Información para el Asistente",
                class_name="text-xl font-semibold text-neutral-800 mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Materia o Área", class_name="block text-sm font-medium"
                    ),
                    rx.el.select(
                        rx.foreach(
                            PiarState.materias, lambda m: rx.el.option(m, value=m)
                        ),
                        name="materia",
                        class_name="mt-1 w-full p-2 border rounded-md",
                    ),
                    class_name="w-full",
                ),
                rx.el.div(
                    rx.el.label(
                        "Periodo Académico", class_name="block text-sm font-medium"
                    ),
                    rx.el.select(
                        rx.foreach(
                            PiarState.periodos, lambda p: rx.el.option(p, value=p)
                        ),
                        name="periodo",
                        class_name="mt-1 w-full p-2 border rounded-md",
                    ),
                    class_name="w-full",
                ),
                class_name="grid md:grid-cols-2 gap-6 mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Dificultad observada del estudiante",
                    class_name="block text-sm font-medium",
                ),
                rx.el.input(
                    placeholder="Ej: Dificultad para mantener la atención en clase...",
                    name="dificultad_observada",
                    class_name="mt-1 w-full p-2 border rounded-md",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Evidencias o ejemplos de la dificultad",
                    class_name="block text-sm font-medium",
                ),
                rx.el.textarea(
                    placeholder="Ej: Se distrae fácilmente, no completa tareas, requiere recordatorios constantes...",
                    name="evidencias",
                    rows=5,
                    class_name="mt-1 w-full p-2 border rounded-md",
                ),
                class_name="mb-6",
            ),
            class_name="p-8 bg-white border border-neutral-200 rounded-xl shadow-sm",
        ),
        rx.el.button(
            rx.icon("bot", class_name="h-6 w-6"),
            on_click=PiarState.toggle_chat,
            class_name="fixed bottom-8 right-8 p-4 bg-indigo-600 text-white rounded-full shadow-lg hover:bg-indigo-700 transition-transform transform hover:scale-110",
        ),
        class_name="w-full max-w-4xl mx-auto pb-24",
    )