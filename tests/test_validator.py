from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("student@example.com") is True
    assert validate_email("not-an-email") is False


def test_validate_phone():
    assert validate_phone("+79991234567") is True
    assert validate_phone("89991234567") is False
    assert validate_phone("+7999123") is False
