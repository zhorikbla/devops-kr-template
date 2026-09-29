"""Небольшой набор функций валидации."""

import re


def validate_email(email: str) -> bool:
    """Проверка базового формата email-адреса."""
    pattern = r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))

