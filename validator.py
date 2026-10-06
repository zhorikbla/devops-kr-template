"""Небольшой набор функций валидации."""

import re


def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    pattern = r"^\+?7\d{10}$"
    return bool(re.match(pattern, phone.replace("-", "").replace(" ", "")))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС по формату XXX-XXX-XXX YY."""
    pattern = r"^\d{3}-\d{3}-\d{3}\s\d{2}$"
    return bool(re.match(pattern, snils))


def validate_email(email: str) -> bool:
    """Проверка базового формата email-адреса."""
    pattern = r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))
