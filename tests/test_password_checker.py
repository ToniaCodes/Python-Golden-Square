import pytest
from  lib.password_checker import PasswordChecker  # Import your PasswordChecker class from the appropriate module

def test_check_short_password_exception():
    password_checker = PasswordChecker()

    with pytest.raises(Exception) as e:
        password_checker.check("short")

    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_check_valid_password():
    password_checker = PasswordChecker()
    result = password_checker.check("validpass")
    assert result is True