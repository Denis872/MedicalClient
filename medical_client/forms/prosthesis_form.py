from .base_form import BaseForm


class ProsthesisForm(BaseForm):
    insert_query = (
        "INSERT INTO prosthesis (study_id, side, fixation, implant_date, revision_date, acetabular_size_mm, cup_anteversion_deg, "
        "cup_inclination_deg, femoral_size_mm, head_size_mm, head_material, polyethylene, fixation_character) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    fields_order = [
        "study_id",
        "side",
        "fixation",
        "implant_date",
        "revision_date",
        "acetabular_size_mm",
        "cup_anteversion_deg",
        "cup_inclination_deg",
        "femoral_size_mm",
        "head_size_mm",
        "head_material",
        "polyethylene",
        "fixation_character",
    ]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID исследования", "study_id")
        self._add_field(1, "Сторона", "side")
        self._add_field(2, "Тип фиксации", "fixation")
        self._add_field(3, "Дата имплантации", "implant_date")
        self._add_field(4, "Дата ревизии", "revision_date")
        self._add_field(5, "Размер чашки (мм)", "acetabular_size_mm")
        self._add_field(6, "Антиверсия (°)", "cup_anteversion_deg")
        self._add_field(7, "Инклинация (°)", "cup_inclination_deg")
        self._add_field(8, "Размер бедренного компонента", "femoral_size_mm")
        self._add_field(9, "Диаметр головки", "head_size_mm")
        self._add_field(10, "Материал головки", "head_material")
        self._add_field(11, "Тип полиэтилена", "polyethylene")
        self._add_field(12, "Характер фиксации", "fixation_character")
        self.add_submit_button(13)

