from validator import validate_email


def test_validate_email():
    assert validate_email("student@example.com") is True
    assert validate_email("not-an-email") is False

