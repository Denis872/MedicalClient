import uuid

from .base_form import BaseForm


class AudioFileForm(BaseForm):
    insert_query = (
        "INSERT INTO audio_file (id, study_id, file_uri, samplerate_hz, duration_sec) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    fields_order = ["id", "study_id", "file_uri", "samplerate_hz", "duration_sec"]

    def _build_form(self) -> None:
        self.columnconfigure(1, weight=1)
        self._add_field(0, "ID файла", "id", default=str(uuid.uuid4()))
        self._add_field(1, "ID исследования", "study_id")
        self._add_field(2, "URI файла", "file_uri")
        self._add_field(3, "Частота дискретизации", "samplerate_hz")
        self._add_field(4, "Длительность (сек)", "duration_sec")
        self.add_submit_button(5)

    def _post_submit(self) -> None:
        super()._post_submit()
        self.entries["id"].insert(0, str(uuid.uuid4()))

