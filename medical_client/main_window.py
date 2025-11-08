import tkinter as tk
from tkinter import ttk
from typing import Dict, Type

from .db import DatabaseManager
from .forms.acoustic_form import AcousticForm
from .forms.audio_file_form import AudioFileForm
from .forms.final_conclusion_form import FinalConclusionForm
from .forms.patient_form import PatientForm
from .forms.prosthesis_form import ProsthesisForm
from .forms.specialist_opinion_form import SpecialistOpinionForm
from .forms.study_form import StudyForm

FORM_REGISTRY: Dict[str, Type[tk.Frame]] = {
    "Пациенты": PatientForm,
    "Исследования": StudyForm,
    "Акустика": AcousticForm,
    "Протез": ProsthesisForm,
    "Аудиофайлы": AudioFileForm,
    "Мнение специалиста": SpecialistOpinionForm,
    "Итоговое заключение": FinalConclusionForm,
}


class MainWindow(ttk.Frame):
    def __init__(self, master: tk.Tk, db: DatabaseManager, user: dict) -> None:
        super().__init__(master)
        self.master = master
        self.db = db
        self.user = user
        self.pack(fill=tk.BOTH, expand=True)

        master.title(f"Медицинский клиент — {user['full_name']}")
        master.geometry("700x500")

        self._build_ui()

    def _build_ui(self) -> None:
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for title, form_cls in FORM_REGISTRY.items():
            frame = form_cls(notebook, self.db)
            notebook.add(frame, text=title)

