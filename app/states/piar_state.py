import reflex as rx
from typing import TypedDict, Optional, Literal


class PiarFormat(TypedDict):
    id: int
    student_name: str
    creation_date: str
    status: str


class CaracterizacionEstudiante(TypedDict):
    descripcion_general: str
    talentos_intereses: str


class ValoracionPedagogica(TypedDict):
    desempeno_academico: str
    competencias_curriculares: str


class ValoracionInterdisciplinar(TypedDict):
    fonoaudiologia: str
    terapia_ocupacional: str
    psicologia: str


class ActaAcuerdos(TypedDict):
    acuerdos: str
    compromisos: str


class Barrera(TypedDict):
    id: int
    materia: str
    periodo: str
    descripcion: str


class Ajuste(TypedDict):
    id: int
    materia: str
    periodo: str
    descripcion: str


class Estrategia(TypedDict):
    id: int
    materia: str
    periodo: str
    descripcion: str


class Seguimiento(TypedDict):
    id: int
    materia: str
    periodo: str
    descripcion: str


MultiEntrySection = Literal["barreras", "ajustes", "estrategias", "seguimiento"]


class PiarState(rx.State):
    """State for the PIAR formats page and form."""

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
    show_piar_form: bool = False
    selected_piar: Optional[PiarFormat] = None
    active_accordion: set[str] = set()
    show_item_modal: bool = False
    editing_section: Optional[MultiEntrySection] = None
    editing_item: Optional[dict] = None
    piar_status: str = "Borrador"
    materias: list[str] = [
        "Matemáticas",
        "Lenguaje",
        "Ciencias Naturales",
        "Ciencias Sociales",
        "Inglés",
    ]
    periodos: list[str] = ["Periodo 1", "Periodo 2", "Periodo 3", "Periodo 4"]
    caracterizacion: CaracterizacionEstudiante = {
        "descripcion_general": "",
        "talentos_intereses": "",
    }
    valoracion_pedagogica: ValoracionPedagogica = {
        "desempeno_academico": "",
        "competencias_curriculares": "",
    }
    valoracion_interdisciplinar: ValoracionInterdisciplinar = {
        "fonoaudiologia": "",
        "terapia_ocupacional": "",
        "psicologia": "",
    }
    barreras: list[Barrera] = []
    ajustes: list[Ajuste] = []
    estrategias: list[Estrategia] = []
    seguimiento: list[Seguimiento] = []
    acta_acuerdos: ActaAcuerdos = {"acuerdos": "", "compromisos": ""}

    @rx.var
    def is_final(self) -> bool:
        return self.piar_status == "Final"

    def _load_mock_data(self):
        self.caracterizacion = {
            "descripcion_general": "Ana es una estudiante activa y participativa en clase.",
            "talentos_intereses": "Muestra un gran interés por el arte y la música.",
        }
        self.barreras = [
            {
                "id": 1,
                "materia": "Matemáticas",
                "periodo": "Periodo 1",
                "descripcion": "Dificultad para comprender conceptos abstractos.",
            },
            {
                "id": 2,
                "materia": "Lenguaje",
                "periodo": "Periodo 1",
                "descripcion": "Problemas con la ortografía y la gramática.",
            },
        ]
        self.ajustes = [
            {
                "id": 1,
                "materia": "Matemáticas",
                "periodo": "Periodo 1",
                "descripcion": "Uso de material manipulativo para conceptos numéricos.",
            }
        ]
        self.piar_status = (
            "Borrador"
            if self.selected_piar and self.selected_piar["status"] != "Completado"
            else "Final"
        )

    @rx.event
    def select_piar_for_editing(self, piar: PiarFormat):
        """Selects a PIAR to edit, loads its data, and shows the form."""
        self.selected_piar = piar
        self._load_mock_data()
        self.show_piar_form = True
        self.active_accordion = set()

    @rx.event
    def return_to_piar_list(self):
        """Returns to the list of PIARs and clears data."""
        self.show_piar_form = False
        self.selected_piar = None
        self.caracterizacion = {"descripcion_general": "", "talentos_intereses": ""}
        self.valoracion_pedagogica = {
            "desempeno_academico": "",
            "competencias_curriculares": "",
        }
        self.valoracion_interdisciplinar = {
            "fonoaudiologia": "",
            "terapia_ocupacional": "",
            "psicologia": "",
        }
        self.barreras = []
        self.ajustes = []
        self.estrategias = []
        self.seguimiento = []
        self.acta_acuerdos = {"acuerdos": "", "compromisos": ""}

    @rx.event
    def toggle_accordion(self, section: str):
        """Toggles the visibility of an accordion section."""
        if section in self.active_accordion:
            self.active_accordion.remove(section)
        else:
            self.active_accordion.add(section)

    @rx.event
    def open_item_modal(self, section: MultiEntrySection, item: Optional[dict] = None):
        self.editing_section = section
        self.editing_item = item
        self.show_item_modal = True

    @rx.event
    def close_item_modal(self):
        self.show_item_modal = False
        self.editing_item = None
        self.editing_section = None

    @rx.event
    def save_item(self, form_data: dict):
        if not self.editing_section:
            return
        section_list = getattr(self, self.editing_section)
        if self.editing_item:
            item_id = self.editing_item["id"]
            index = next(
                (i for i, item in enumerate(section_list) if item["id"] == item_id),
                None,
            )
            if index is not None:
                section_list[index].update(form_data)
        else:
            new_id = max((item["id"] for item in section_list), default=0) + 1
            new_item = {"id": new_id, **form_data}
            section_list.append(new_item)
        self.close_item_modal()
        return rx.toast.success("Registro guardado.")

    @rx.event
    def delete_item(self, section: MultiEntrySection, item_id: int):
        section_list = getattr(self, section)
        setattr(self, section, [item for item in section_list if item["id"] != item_id])
        return rx.toast.info("Registro eliminado.")

    @rx.event
    def update_single_entry_field(self, section: str, field: str, value: str):
        """Autosave for single-entry text fields."""
        section_data = getattr(self, section)
        section_data[field] = value