from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Dict, Optional

from ..db import DatabaseError, DatabaseManager


class BaseForm(tk.Frame):
    table_name: str = ""
    insert_query: str = ""

    fields_order: list[str]

    def __init__(self, master: tk.Widget, db: DatabaseManager) -> None:
        super().__init__(master)
        if not self.insert_query:
            raise ValueError("insert_query must be defined in child form")
        if not hasattr(self, "fields_order"):
            raise ValueError("fields_order must be defined in child form")

        self.db = db
        self.entries: Dict[str, tk.Entry] = {}
        self._build_form()

    def _build_form(self) -> None:
        raise NotImplementedError

    def _add_field(self, row: int, label: str, name: str, *, width: int = 40, default: Optional[str] = None, show: Optional[str] = None) -> tk.Entry:
        tk.Label(self, text=label).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(self, width=width, show=show)
        entry.grid(row=row, column=1, sticky="ew", padx=10, pady=5)
        if default is not None:
            entry.insert(0, default)
        self.entries[name] = entry
        return entry

    def _collect_data(self) -> Dict[str, Optional[str]]:
        return {name: entry.get().strip() or None for name, entry in self.entries.items()}

    def _submit(self) -> None:
        values = self._collect_data()
        params = [values.get(field) for field in self.fields_order]
        try:
            self.db.execute(self.insert_query, params)
        except DatabaseError as exc:
            messagebox.showerror("Ошибка", str(exc))
            return

        messagebox.showinfo("Успех", "Запись сохранена")
        self._post_submit()

    def add_submit_button(self, row: int) -> None:
        submit_btn = tk.Button(self, text="Сохранить", command=self._submit)
        submit_btn.grid(row=row, column=0, columnspan=2, pady=10)

    def _post_submit(self) -> None:
        for entry in self.entries.values():
            entry.delete(0, tk.END)


