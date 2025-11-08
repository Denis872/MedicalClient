from .base_form import BaseForm


class AcousticForm(BaseForm):
    insert_query = (
        "INSERT INTO acoustic (study_id, width_cat, asymmetry_cat, peak_cat, amplitude_cat, threshold, width_hz, asymmetry, peak, "
        "stat_value, impulse_height, amplitude_db) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    fields_order = [
        "study_id",
        "width_cat",
        "asymmetry_cat",
        "peak_cat",
        "amplitude_cat",
        "threshold",
        "width_hz",
        "asymmetry",
        "peak",
        "stat_value",
        "impulse_height",
        "amplitude_db",
    ]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID исследования", "study_id")
        self._add_field(1, "Категория ширины", "width_cat")
        self._add_field(2, "Категория асимметрии", "asymmetry_cat")
        self._add_field(3, "Категория пика", "peak_cat")
        self._add_field(4, "Категория амплитуды", "amplitude_cat")
        self._add_field(5, "Порог", "threshold")
        self._add_field(6, "Ширина (Гц)", "width_hz")
        self._add_field(7, "Асимметрия", "asymmetry")
        self._add_field(8, "Пик", "peak")
        self._add_field(9, "Стат. значение", "stat_value")
        self._add_field(10, "Высота импульса", "impulse_height")
        self._add_field(11, "Амплитуда (дБ)", "amplitude_db")
        self.add_submit_button(12)

