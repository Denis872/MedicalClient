import uuid

from .base_form import BaseForm


class PatientForm(BaseForm):
    insert_query = (
        "INSERT INTO patient (id, mrn, dob, sex) "
        "VALUES (%s, %s, %s, %s)"
    )
    fields_order = ["id", "mrn", "dob", "sex"]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID (UUID)", "id", default=str(uuid.uuid4()))
        self._add_field(1, "№ истории болезни", "mrn")
        self._add_field(2, "Дата рождения (ГГГГ-ММ-ДД)", "dob")
        self._add_field(3, "Пол (sex_t)", "sex")
        self.add_submit_button(4)

    def _post_submit(self) -> None:
        super()._post_submit()
        self.entries["id"].insert(0, str(uuid.uuid4()))

