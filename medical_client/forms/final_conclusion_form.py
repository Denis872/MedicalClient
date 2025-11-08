from .base_form import BaseForm


class FinalConclusionForm(BaseForm):
    insert_query = (
        "INSERT INTO final_conclusion (study_id, final_diagnosis_code, summary, approved_by) "
        "VALUES (%s, %s, %s, %s)"
    )
    fields_order = ["study_id", "final_diagnosis_code", "summary", "approved_by"]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID исследования", "study_id")
        self._add_field(1, "Код итогового диагноза", "final_diagnosis_code")
        self._add_field(2, "Заключение", "summary", width=60)
        self._add_field(3, "Утвердил (UUID)", "approved_by")
        self.add_submit_button(4)

