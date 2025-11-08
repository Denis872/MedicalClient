import logging
from contextlib import contextmanager
from typing import Any, Dict, Iterable, Optional

import psycopg2
from psycopg2.extras import RealDictCursor


logger = logging.getLogger(__name__)


class DatabaseError(Exception):
    """Raised when a database operation fails."""


class DatabaseManager:
    """A thin wrapper around psycopg2 with convenience helpers."""

    def __init__(self, dsn: str) -> None:
        self._dsn = dsn
        self._connection_kwargs: Dict[str, Any] = {}
        logger.debug("DatabaseManager initialized with DSN: %s", dsn)

    @contextmanager
    def connection(self):
        conn = None
        try:
            conn = psycopg2.connect(self._dsn, cursor_factory=RealDictCursor, **self._connection_kwargs)
            yield conn
        except psycopg2.Error as exc:
            logger.exception("Database connection error")
            raise DatabaseError("Не удалось подключиться к базе данных.") from exc
        finally:
            if conn is not None:
                conn.close()

    def execute(
        self,
        query: str,
        params: Optional[Iterable[Any]] = None,
        *,
        fetchone: bool = False,
        fetchall: bool = False,
    ) -> Any:
        logger.debug("Executing query: %s with params: %s", query, params)
        with self.connection() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    if fetchone:
                        result = cur.fetchone()
                        logger.debug("Fetchone result: %s", result)
                        return result
                    if fetchall:
                        result = cur.fetchall()
                        logger.debug("Fetchall result: %s", result)
                        return result
                    conn.commit()
            except psycopg2.Error as exc:
                conn.rollback()
                logger.exception("Database query error")
                raise DatabaseError("Ошибка выполнения запроса к базе данных.") from exc

    def verify_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Validate a user's credentials.

        The method assumes that the app_user table contains a password_hash column
        generated with the crypt function from the pgcrypto extension.
        """
        query = (
            "SELECT id, full_name, role, email "
            "FROM app_user "
            "WHERE email = %s AND password_hash = crypt(%s, password_hash)"
        )
        try:
            user = self.execute(query, (email, password), fetchone=True)
            return user
        except DatabaseError:
            raise

