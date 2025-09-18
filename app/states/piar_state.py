import reflex as rx
from typing import TypedDict, Optional, Literal


class PiarFormat(TypedDict):
    id: int
    student_name: str
    creation_date: str
    status: str


class CaracterizacionEstudiante(TypedDict):
    estilo_ritmo_aprendizaje: str
    fortalezas: str
    intereses: str
    necesidades_especiales: str
    contexto_familiar_social: str


class ValoracionArea(TypedDict):
    nivel: str
    observaciones: str


class ValoracionPedagogica(TypedDict):
    lectoescritura: ValoracionArea
    matematicas: ValoracionArea
    ciencias_naturales: ValoracionArea
    ciencias_sociales: ValoracionArea
    otras_areas: ValoracionArea


class ValoracionInterdisciplinarItem(TypedDict):
    id: int
    disciplina: str
    profesional_responsable: str
    fecha_concepto: str
    resumen_concepto: str
    recomendaciones: str


class ActaAcuerdos(TypedDict):
    compromisos_institucion: str
    compromisos_familia: str
    compromisos_estudiante: str
    compromisos_apoyos_externos: str
    firmas: str
    fecha_firma: str


class Barrera(TypedDict):
    id: int
    materia: str
    periodo: str
    tipo_barrera: str
    descripcion: str
    evidencias: str


class Ajuste(TypedDict):
    id: int
    materia: str
    periodo: str
    categoria_ajuste: str
    descripcion: str
    recursos_requeridos: str


class Estrategia(TypedDict):
    id: int
    materia: str
    periodo: str
    metodo_sugerido: str
    descripcion: str


class Seguimiento(TypedDict):
    id: int
    materia: str
    periodo: str
    observaciones_avance: str
    evidencias_recolectadas: str
    acciones_mejora: str


MultiEntrySection = Literal[
    "valoracion_interdisciplinar", "barreras", "ajustes", "estrategias", "seguimiento"
]


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
    show_assistant_form: bool = False
    selected_piar: Optional[PiarFormat] = None
    active_accordion: set[str] = set()
    show_item_modal: bool = False
    editing_section: Optional[MultiEntrySection] = None
    editing_item: Optional[dict] = None
    piar_status: str = "Borrador"
    materias: list[str] = [
        "Lengua",
        "Matemáticas",
        "Ciencias Naturales",
        "Ciencias Sociales",
        "Arte",
        "Educación Física",
        "Tecnología",
        "Inglés",
    ]
    periodos: list[str] = [
        "Bimestre 1",
        "Bimestre 2",
        "Bimestre 3",
        "Bimestre 4",
        "Trimestre 1",
        "Trimestre 2",
        "Trimestre 3",
    ]
    niveles_desempeno: list[str] = [
        "Alto",
        "Medio",
        "Bajo",
        "Desempeño Satisfactorio",
        "En proceso",
    ]
    tipos_barrera: list[str] = [
        "Física",
        "Comunicativa",
        "Curricular",
        "Actitudinal",
        "Otra",
    ]
    categorias_ajuste: list[str] = [
        "Curricular",
        "Tiempo de evaluación",
        "Materiales",
        "Participación",
        "Apoyos humanos",
    ]
    caracterizacion: CaracterizacionEstudiante = {
        "estilo_ritmo_aprendizaje": "",
        "fortalezas": "",
        "intereses": "",
        "necesidades_especiales": "",
        "contexto_familiar_social": "",
    }
    valoracion_pedagogica: ValoracionPedagogica = {
        "lectoescritura": {"nivel": "", "observaciones": ""},
        "matematicas": {"nivel": "", "observaciones": ""},
        "ciencias_naturales": {"nivel": "", "observaciones": ""},
        "ciencias_sociales": {"nivel": "", "observaciones": ""},
        "otras_areas": {"nivel": "", "observaciones": ""},
    }
    valoracion_observaciones_generales: str = ""
    valoracion_interdisciplinar: list[ValoracionInterdisciplinarItem] = []
    barreras: list[Barrera] = []
    ajustes: list[Ajuste] = []
    estrategias: list[Estrategia] = []
    seguimiento: list[Seguimiento] = []
    acta_acuerdos: ActaAcuerdos = {
        "compromisos_institucion": "",
        "compromisos_familia": "",
        "compromisos_estudiante": "",
        "compromisos_apoyos_externos": "",
        "firmas": "",
        "fecha_firma": "",
    }
    show_chat: bool = False
    chat_messages: list[dict] = []
    assistant_form_data: dict = {
        "materia": "",
        "periodo": "",
        "dificultad_observada": "",
        "evidencias": "",
    }

    @rx.var
    def is_final(self) -> bool:
        return self.piar_status == "Final"

    def _load_mock_data(self):
        self.caracterizacion = {
            "estilo_ritmo_aprendizaje": "Visual y práctico",
            "fortalezas": "Creatividad, perseverancia.",
            "intereses": "Dibujo, construcción con bloques.",
            "necesidades_especiales": "Dislexia diagnosticada.",
            "contexto_familiar_social": "Apoyo familiar constante.",
        }
        self.barreras = [
            {
                "id": 1,
                "materia": "Matemáticas",
                "periodo": "Trimestre 1",
                "tipo_barrera": "Curricular",
                "descripcion": "Dificultad para comprender conceptos abstractos sin apoyo visual.",
                "evidencias": "Bajo rendimiento en evaluaciones escritas sin gráficos.",
            }
        ]
        self.ajustes = [
            {
                "id": 1,
                "materia": "Matemáticas",
                "periodo": "Trimestre 1",
                "categoria_ajuste": "Materiales",
                "descripcion": "Proporcionar material concreto y manipulable (ábacos, bloques).",
                "recursos_requeridos": "Kit de matemáticas manipulativas.",
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
    def open_assistant_form(self, piar: PiarFormat):
        self.selected_piar = piar
        self._load_mock_data()
        self.show_assistant_form = True
        self.show_chat = False
        self.chat_messages = []

    @rx.event
    def return_to_piar_list(self):
        """Returns to the list of PIARs and clears data."""
        self.show_piar_form = False
        self.show_assistant_form = False
        self.selected_piar = None
        self.caracterizacion = {
            "estilo_ritmo_aprendizaje": "",
            "fortalezas": "",
            "intereses": "",
            "necesidades_especiales": "",
            "contexto_familiar_social": "",
        }
        self.valoracion_pedagogica = {
            "lectoescritura": {"nivel": "", "observaciones": ""},
            "matematicas": {"nivel": "", "observaciones": ""},
            "ciencias_naturales": {"nivel": "", "observaciones": ""},
            "ciencias_sociales": {"nivel": "", "observaciones": ""},
            "otras_areas": {"nivel": "", "observaciones": ""},
        }
        self.valoracion_observaciones_generales = ""
        self.valoracion_interdisciplinar = []
        self.barreras = []
        self.ajustes = []
        self.estrategias = []
        self.seguimiento = []
        self.acta_acuerdos = {
            "compromisos_institucion": "",
            "compromisos_familia": "",
            "compromisos_estudiante": "",
            "compromisos_apoyos_externos": "",
            "firmas": "",
            "fecha_firma": "",
        }

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
    def toggle_chat(self):
        self.show_chat = not self.show_chat
        if self.show_chat and (not self.chat_messages):
            student_name = (
                self.selected_piar["student_name"] if self.selected_piar else "docente"
            )
            self.chat_messages.append(
                {
                    "sender": "assistant",
                    "message": f"¡Hola! Soy tu asistente pedagógico. ¿Cómo puedo ayudarte hoy a definir las barreras y ajustes para {student_name}?",
                }
            )

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
                updated_item = dict(section_list[index])
                updated_item.update(form_data)
                section_list[index] = updated_item
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

    @rx.event
    def update_valoracion_pedagogica_field(self, area: str, field: str, value: str):
        self.valoracion_pedagogica[area][field] = value