"""Формы для внесения данных в разные таблицы."""

from .acoustic_form import AcousticForm
from .audio_file_form import AudioFileForm
from .final_conclusion_form import FinalConclusionForm
from .patient_form import PatientForm
from .prosthesis_form import ProsthesisForm
from .specialist_opinion_form import SpecialistOpinionForm
from .study_form import StudyForm

__all__ = [
    "AcousticForm",
    "AudioFileForm",
    "FinalConclusionForm",
    "PatientForm",
    "ProsthesisForm",
    "SpecialistOpinionForm",
    "StudyForm",
]

