import uuid

from .base_form import BaseForm


class SpecialistOpinionForm(BaseForm):
    insert_query = (
        "INSERT INTO specialist_opinion (id, study_id, specialist_id, diagnosis_code, comment) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    fields_order = ["id", "study_id", "specialist_id", "diagnosis_code", "comment"]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID заключения", "id", default=str(uuid.uuid4()))
        self._add_field(1, "ID исследования", "study_id")
        self._add_field(2, "ID специалиста", "specialist_id")
        self._add_field(3, "Код диагноза", "diagnosis_code")
        self._add_field(4, "Комментарий", "comment", width=60)
        self.add_submit_button(5)

    def _post_submit(self) -> None:
        super()._post_submit()
        self.entries["id"].insert(0, str(uuid.uuid4()))

