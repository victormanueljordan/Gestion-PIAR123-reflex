import reflex as rx
from typing import TypedDict, Optional
import logging


class Grupo(TypedDict):
    id: int
    nombre: str


class Grado(TypedDict):
    id: int
    nombre: str
    grupos: list[Grupo]


class Asignatura(TypedDict):
    id: int
    nombre: str


class Area(TypedDict):
    id: int
    nombre: str
    asignaturas: list[Asignatura]


class Docente(TypedDict):
    id: int
    nombre: str
    email: str
    telefono: str
    roles: list[str]


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


class Periodo(TypedDict):
    id: int
    nombre: str
    fecha_inicio: str
    fecha_fin: str
    activo: bool


class AnoLectivoData(TypedDict):
    ano_activo: int
    fecha_inicio: str
    fecha_fin: str
    esquema_periodos: str
    fecha_limite_cierre: str


class CatalogoItem(TypedDict):
    id: int
    nombre: str


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
    def update_ano_lectivo_field(self, field: str, value: str):
        if field == "ano_activo":
            try:
                self.ano_lectivo[field] = int(value)
            except (ValueError, TypeError) as e:
                logging.exception(f"Error converting year to int: {e}")
                return rx.toast.error("El año debe ser un número.")
        else:
            self.ano_lectivo[field] = value
        return rx.toast.success("Campo de año lectivo actualizado")

    @rx.event
    def add_periodo(self):
        new_id = max((p["id"] for p in self.periodos), default=0) + 1
        self.periodos.append(
            {
                "id": new_id,
                "nombre": f"Nuevo Periodo {new_id}",
                "fecha_inicio": "",
                "fecha_fin": "",
                "activo": False,
            }
        )
        return rx.toast.success("Nuevo periodo añadido.")

    @rx.event
    def update_periodo(self, periodo_id: int, field: str, value):
        for i, periodo in enumerate(self.periodos):
            if periodo["id"] == periodo_id:
                self.periodos[i][field] = value
                break
        return rx.toast.success("Periodo actualizado.")

    @rx.event
    def delete_periodo(self, periodo_id: int):
        self.periodos = [p for p in self.periodos if p["id"] != periodo_id]
        return rx.toast.error("Periodo eliminado.")

    def _get_next_catalogo_id(self, catalogo_name: str) -> int:
        catalogo_list = getattr(self, catalogo_name)
        if not catalogo_list:
            return 1
        return max((item["id"] for item in catalogo_list)) + 1

    @rx.event
    def add_catalogo_item(self, catalogo_name: str, form_data: dict):
        if not form_data.get("nombre"):
            return rx.toast.error("El nombre no puede estar vacío.")
        catalogo_list = getattr(self, catalogo_name)
        new_id = self._get_next_catalogo_id(catalogo_name)
        catalogo_list.append({"id": new_id, "nombre": form_data["nombre"]})
        return rx.toast.success("Elemento añadido.")

    @rx.event
    def update_catalogo_item(self, catalogo_name: str, item_id: int, new_name: str):
        catalogo_list = getattr(self, catalogo_name)
        for i, item in enumerate(catalogo_list):
            if item["id"] == item_id:
                catalogo_list[i]["nombre"] = new_name
                break
        return rx.toast.success("Elemento actualizado.")

    @rx.event
    def delete_catalogo_item(self, catalogo_name: str, item_id: int):
        catalogo_list = getattr(self, catalogo_name)
        setattr(
            self,
            catalogo_name,
            [item for item in catalogo_list if item["id"] != item_id],
        )
        return rx.toast.error("Elemento eliminado.")

    ano_lectivo: AnoLectivoData = {
        "ano_activo": 2024,
        "fecha_inicio": "2024-02-01",
        "fecha_fin": "2024-11-30",
        "esquema_periodos": "Bimestres",
        "fecha_limite_cierre": "2024-11-15",
    }
    periodos: list[Periodo] = [
        {
            "id": 1,
            "nombre": "Bimestre 1",
            "fecha_inicio": "2024-02-01",
            "fecha_fin": "2024-04-05",
            "activo": False,
        },
        {
            "id": 2,
            "nombre": "Bimestre 2",
            "fecha_inicio": "2024-04-08",
            "fecha_fin": "2024-06-14",
            "activo": True,
        },
    ]
    catalogo_tipos_barrera: list[CatalogoItem] = [
        {"id": 1, "nombre": "Física"},
        {"id": 2, "nombre": "Comunicativa"},
    ]
    catalogo_categorias_ajuste: list[CatalogoItem] = [
        {"id": 1, "nombre": "Curricular"},
        {"id": 2, "nombre": "Tiempos de evaluación"},
    ]
    catalogo_metodos: list[CatalogoItem] = [
        {"id": 1, "nombre": "Aprendizaje cooperativo"},
        {"id": 2, "nombre": "Proyectos"},
    ]
    catalogo_tipos_evidencia: list[CatalogoItem] = [
        {"id": 1, "nombre": "Trabajos escritos"},
        {"id": 2, "nombre": "Observaciones en clase"},
    ]
    catalogo_roles: list[CatalogoItem] = [
        {"id": 1, "nombre": "Docente de aula"},
        {"id": 2, "nombre": "Docente de apoyo"},
        {"id": 3, "nombre": "Coordinador"},
        {"id": 4, "nombre": "Rector"},
        {"id": 5, "nombre": "Psicólogo"},
    ]
    docentes: list[Docente] = [
        {
            "id": 1,
            "nombre": "Ana María López",
            "email": "ana.lopez@example.com",
            "telefono": "3101234567",
            "roles": ["Docente de aula", "Coordinador"],
        },
        {
            "id": 2,
            "nombre": "Carlos Restrepo",
            "email": "carlos.restrepo@example.com",
            "telefono": "3119876543",
            "roles": ["Docente de apoyo"],
        },
    ]
    grados: list[Grado] = [
        {
            "id": 1,
            "nombre": "Primero",
            "grupos": [{"id": 101, "nombre": "1-A"}, {"id": 102, "nombre": "1-B"}],
        },
        {"id": 2, "nombre": "Segundo", "grupos": [{"id": 201, "nombre": "2-A"}]},
    ]
    areas: list[Area] = [
        {
            "id": 1,
            "nombre": "Ciencias Naturales",
            "asignaturas": [
                {"id": 101, "nombre": "Biología"},
                {"id": 102, "nombre": "Química"},
            ],
        },
        {
            "id": 2,
            "nombre": "Matemáticas",
            "asignaturas": [{"id": 201, "nombre": "Álgebra"}],
        },
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

    def _get_next_docente_id(self) -> int:
        if not self.docentes:
            return 1
        return max((d["id"] for d in self.docentes)) + 1

    @rx.event
    def add_docente(self):
        new_id = self._get_next_docente_id()
        self.docentes.append(
            {
                "id": new_id,
                "nombre": f"Nuevo Docente {new_id}",
                "email": "",
                "telefono": "",
                "roles": [],
            }
        )
        return rx.toast.success("Nuevo docente añadido.")

    @rx.event
    def update_docente(self, docente_id: int, field: str, value: str):
        for i, docente in enumerate(self.docentes):
            if docente["id"] == docente_id:
                self.docentes[i][field] = value
                break
        return rx.toast.success("Docente actualizado.")

    @rx.event
    def delete_docente(self, docente_id: int):
        self.docentes = [d for d in self.docentes if d["id"] != docente_id]
        return rx.toast.error("Docente eliminado.")

    @rx.event
    def toggle_docente_rol(self, docente_id: int, rol_nombre: str):
        for i, docente in enumerate(self.docentes):
            if docente["id"] == docente_id:
                current_roles = self.docentes[i]["roles"]
                if rol_nombre in current_roles:
                    current_roles.remove(rol_nombre)
                else:
                    current_roles.append(rol_nombre)
                break
        return rx.toast.success("Roles del docente actualizados.")

    @rx.event
    def add_grado(self):
        new_id = max((g["id"] for g in self.grados), default=0) + 1
        self.grados.append(
            {"id": new_id, "nombre": f"Nuevo Grado {new_id}", "grupos": []}
        )

    @rx.event
    def update_grado_nombre(self, grado_id: int, nombre: str):
        for i, grado in enumerate(self.grados):
            if grado["id"] == grado_id:
                self.grados[i]["nombre"] = nombre
                break

    @rx.event
    def delete_grado(self, grado_id: int):
        self.grados = [g for g in self.grados if g["id"] != grado_id]

    @rx.event
    def add_grupo(self, grado_id: int):
        for i, grado in enumerate(self.grados):
            if grado["id"] == grado_id:
                new_id = (
                    max((g["id"] for g in grado["grupos"]), default=grado_id * 100) + 1
                )
                self.grados[i]["grupos"].append(
                    {"id": new_id, "nombre": f"Grupo {new_id}"}
                )
                break

    @rx.event
    def update_grupo_nombre(self, grado_id: int, grupo_id: int, nombre: str):
        for i, grado in enumerate(self.grados):
            if grado["id"] == grado_id:
                for j, grupo in enumerate(grado["grupos"]):
                    if grupo["id"] == grupo_id:
                        self.grados[i]["grupos"][j]["nombre"] = nombre
                        break
                break

    @rx.event
    def delete_grupo(self, grado_id: int, grupo_id: int):
        for i, grado in enumerate(self.grados):
            if grado["id"] == grado_id:
                self.grados[i]["grupos"] = [
                    g for g in grado["grupos"] if g["id"] != grupo_id
                ]
                break

    @rx.event
    def add_area(self):
        new_id = max((a["id"] for a in self.areas), default=0) + 1
        self.areas.append(
            {"id": new_id, "nombre": f"Nueva Área {new_id}", "asignaturas": []}
        )

    @rx.event
    def update_area_nombre(self, area_id: int, nombre: str):
        for i, area in enumerate(self.areas):
            if area["id"] == area_id:
                self.areas[i]["nombre"] = nombre
                break

    @rx.event
    def delete_area(self, area_id: int):
        self.areas = [a for a in self.areas if a["id"] != area_id]

    @rx.event
    def add_asignatura(self, area_id: int):
        for i, area in enumerate(self.areas):
            if area["id"] == area_id:
                new_id = (
                    max((a["id"] for a in area["asignaturas"]), default=area_id * 100)
                    + 1
                )
                self.areas[i]["asignaturas"].append(
                    {"id": new_id, "nombre": f"Asignatura {new_id}"}
                )
                break

    @rx.event
    def update_asignatura_nombre(self, area_id: int, asignatura_id: int, nombre: str):
        for i, area in enumerate(self.areas):
            if area["id"] == area_id:
                for j, asignatura in enumerate(area["asignaturas"]):
                    if asignatura["id"] == asignatura_id:
                        self.areas[i]["asignaturas"][j]["nombre"] = nombre
                        break
                break

    @rx.event
    def delete_asignatura(self, area_id: int, asignatura_id: int):
        for i, area in enumerate(self.areas):
            if area["id"] == area_id:
                self.areas[i]["asignaturas"] = [
                    a for a in area["asignaturas"] if a["id"] != asignatura_id
                ]
                break