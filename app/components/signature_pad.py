import reflex as rx
from app.states.piar_state import PiarState


def signature_pad_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
            on_click=PiarState.close_signature_pad,
        ),
        rx.el.div(
            rx.el.h2("Añadir Firma", class_name="text-lg font-bold p-4 border-b"),
            rx.el.div(
                rx.el.input(
                    placeholder="Nombre completo del firmante",
                    on_change=PiarState.set_current_signer_name,
                    class_name="w-full p-2 border rounded-md mb-2",
                ),
                rx.el.input(
                    placeholder="Rol (Ej: Acudiente, Docente)",
                    on_change=PiarState.set_current_signer_role,
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="p-4",
            ),
            rx.el.div(
                rx.el.div(
                    "Espacio para la firma (Canvas)",
                    class_name="w-full h-48 border-2 border-dashed rounded-md flex items-center justify-center text-neutral-500 bg-neutral-50",
                ),
                id="signature-canvas",
                class_name="p-4",
            ),
            rx.el.div(
                rx.el.button(
                    "Cancelar",
                    on_click=PiarState.close_signature_pad,
                    class_name="px-4 py-2 bg-neutral-200 rounded-lg",
                ),
                rx.el.button(
                    "Guardar Firma",
                    on_click=lambda: PiarState.save_signature(
                        "data:image/png;base64,..."
                    ),
                    class_name="px-4 py-2 bg-indigo-600 text-white rounded-lg",
                ),
                class_name="flex justify-end gap-4 p-4 border-t",
            ),
            class_name="bg-white rounded-xl shadow-2xl w-full max-w-lg z-50",
        ),
        open=PiarState.show_signature_pad,
        class_name="fixed inset-0 open:flex items-center justify-center p-4 z-50",
    )