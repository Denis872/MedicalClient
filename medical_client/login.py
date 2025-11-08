import tkinter as tk
from tkinter import messagebox
from typing import Callable, Optional

from .db import DatabaseError, DatabaseManager


class LoginWindow(tk.Toplevel):
    def __init__(self, master: tk.Tk, db: DatabaseManager, on_success: Callable[[dict], None]) -> None:
        super().__init__(master)
        self.title("Авторизация")
        self.resizable(False, False)
        self.db = db
        self.on_success = on_success
        self.user: Optional[dict] = None

        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self._build_ui()

    def _build_ui(self) -> None:
        tk.Label(self, text="E-mail:").grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.grid(row=0, column=1, padx=10, pady=(10, 5))
        self.email_entry.focus()

        tk.Label(self, text="Пароль:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(self, text="Войти", command=self._authenticate)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.bind("<Return>", lambda event: self._authenticate())

    def _authenticate(self) -> None:
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            messagebox.showwarning("Ошибка", "Введите e-mail и пароль")
            return

        try:
            user = self.db.verify_user(email, password)
        except DatabaseError as exc:
            messagebox.showerror("Ошибка", str(exc))
            return

        if not user:
            messagebox.showerror("Ошибка", "Неверный e-mail или пароль")
            return

        self.user = user
        self.on_success(user)
        self.destroy()

    def _on_close(self) -> None:
        if messagebox.askyesno("Выход", "Закрыть приложение?"):
            self.master.destroy()

