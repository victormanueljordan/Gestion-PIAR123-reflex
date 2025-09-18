import reflex as rx
from typing import TypedDict, Optional


class Sede(TypedDict):
    id: int
    nombre: str
    direccion: str
    ciudad: str
    telefono: str
    email: str


class InstitucionData(TypedDict):
    nombre_oficial: str
    codigo_dane: str
    naturaleza: str
    calendario: str
    niveles: list[str]
    jornadas: list[str]
    rector_nombre: str
    rector_email: str
    rector_telefono: str
    logo: str
    color_primario: str
    color_secundario: str


class SettingsState(rx.State):
    """State for the settings page."""

    active_accordion: str = "institucion"
    institucion: InstitucionData = {
        "nombre_oficial": "Institución Educativa Ejemplo",
        "codigo_dane": "123456789012",
        "naturaleza": "Pública",
        "calendario": "A",
        "niveles": ["Preescolar", "Básica"],
        "jornadas": ["Mañana", "Tarde"],
        "rector_nombre": "Juan Pérez",
        "rector_email": "rector@example.com",
        "rector_telefono": "3001234567",
        "logo": "",
        "color_primario": "#6366F1",
        "color_secundario": "#F3F4F6",
    }
    sedes: list[Sede] = [
        {
            "id": 1,
            "nombre": "Sede Principal",
            "direccion": "Calle Falsa 123",
            "ciudad": "Ciudad Ejemplo",
            "telefono": "3009876543",
            "email": "principal@example.com",
        }
    ]

    @rx.event
    def set_active_accordion(self, accordion_key: str):
        self.active_accordion = (
            accordion_key if self.active_accordion != accordion_key else ""
        )

    @rx.event
    def update_institucion_field(self, field: str, value: str):
        self.institucion[field] = value
        return rx.toast.success("Campo actualizado")

    @rx.event
    def toggle_institucion_multiselect(self, field: str, value: str):
        current_values = self.institucion[field]
        if value in current_values:
            current_values.remove(value)
        else:
            current_values.append(value)
        self.institucion[field] = current_values
        return rx.toast.success("Selección actualizada")

    @rx.event
    async def handle_logo_upload(self, files: list[rx.UploadFile]):
        if not files:
            return rx.toast.error("No se seleccionó ningún archivo.")
        file = files[0]
        upload_data = await file.read()
        outfile = rx.get_upload_dir() / file.name
        with outfile.open("wb") as file_object:
            file_object.write(upload_data)
        self.institucion["logo"] = file.name
        return rx.toast.success("Logo subido correctamente.")

    @rx.var
    def logo_url(self) -> str:
        if self.institucion["logo"]:
            return rx.get_upload_url(self.institucion["logo"])
        return "/placeholder.svg"

    def _get_next_sede_id(self) -> int:
        if not self.sedes:
            return 1
        return max((s["id"] for s in self.sedes)) + 1

    @rx.event
    def add_sede(self):
        new_id = self._get_next_sede_id()
        self.sedes.append(
            {
                "id": new_id,
                "nombre": f"Nueva Sede {new_id}",
                "direccion": "",
                "ciudad": "",
                "telefono": "",
                "email": "",
            }
        )
        return rx.toast.success("Nueva sede añadida.")

    @rx.event
    def update_sede(self, sede_id: int, field: str, value: str):
        for i, sede in enumerate(self.sedes):
            if sede["id"] == sede_id:
                self.sedes[i][field] = value
                break
        return rx.toast.success("Sede actualizada.")

    @rx.event
    def delete_sede(self, sede_id: int):
        self.sedes = [s for s in self.sedes if s["id"] != sede_id]
        return rx.toast.error("Sede eliminada.")