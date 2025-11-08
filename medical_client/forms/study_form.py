import uuid

from .base_form import BaseForm


class StudyForm(BaseForm):
    insert_query = (
        "INSERT INTO study (id, patient_id, study_dt, diagnosis_code, height_cm, weight_kg, bmi, age_years, status, created_by) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    fields_order = [
        "id",
        "patient_id",
        "study_dt",
        "diagnosis_code",
        "height_cm",
        "weight_kg",
        "bmi",
        "age_years",
        "status",
        "created_by",
    ]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID (UUID)", "id", default=str(uuid.uuid4()))
        self._add_field(1, "ID пациента", "patient_id")
        self._add_field(2, "Дата/время исследования", "study_dt")
        self._add_field(3, "Код диагноза", "diagnosis_code")
        self._add_field(4, "Рост (см)", "height_cm")
        self._add_field(5, "Вес (кг)", "weight_kg")
        self._add_field(6, "BMI", "bmi")
        self._add_field(7, "Возраст", "age_years")
        self._add_field(8, "Статус", "status")
        self._add_field(9, "Создано пользователем (UUID)", "created_by")
        self.add_submit_button(10)

    def _post_submit(self) -> None:
        super()._post_submit()
        self.entries["id"].insert(0, str(uuid.uuid4()))

