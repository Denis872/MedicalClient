import configparser
import logging
import os
import sys
import tkinter as tk
from tkinter import messagebox

from .db import DatabaseManager, DatabaseError
from .login import LoginWindow
from .main_window import MainWindow


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


CONFIG_LOCATIONS = [
    os.path.join(os.getcwd(), "config.ini"),
    os.path.join(os.getcwd(), "config.example.ini"),
]


def load_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    read_files = config.read(CONFIG_LOCATIONS)
    if not read_files:
        messagebox.showerror(
            "Конфигурация",
            "Файл config.ini не найден. Создайте его на основе config.example.ini",
        )
        raise SystemExit(1)
    return config


def build_dsn(config: configparser.ConfigParser) -> str:
    try:
        params = config["database"]
    except KeyError as exc:
        messagebox.showerror("Конфигурация", "Секция [database] отсутствует в config.ini")
        raise SystemExit(1) from exc

    try:
        return "dbname={dbname} user={user} password={password} host={host} port={port}".format(**params)
    except KeyError as exc:
        messagebox.showerror("Конфигурация", f"Не хватает параметра {exc.args[0]} в секции [database]")
        raise SystemExit(1) from exc


def main() -> None:
    root = tk.Tk()
    root.withdraw()

    try:
        config = load_config()
        dsn = build_dsn(config)
        db = DatabaseManager(dsn)
    except SystemExit:
        root.destroy()
        return
    except Exception as exc:
        messagebox.showerror("Ошибка", f"Не удалось инициализировать приложение: {exc}")
        root.destroy()
        return

    def on_login_success(user: dict) -> None:
        root.deiconify()
        MainWindow(root, db, user)

    LoginWindow(root, db, on_login_success)
    try:
        root.mainloop()
    except DatabaseError as exc:
        messagebox.showerror("Ошибка БД", str(exc))
    except Exception:
        logger.exception("Необработанная ошибка в главном цикле")
        messagebox.showerror("Критическая ошибка", "Произошла непредвиденная ошибка. Подробности в логах.")
        sys.exit(1)


if __name__ == "__main__":
    main()

