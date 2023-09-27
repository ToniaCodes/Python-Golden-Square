from lib.report_length import *

def test_report_length():
    result = report_length("Hello, World!")
    assert result == "This string was 13 characters long."
    

def test_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."
    

def test_unicode_characters():
    result = report_length("%&$")
    assert result == "This string was 3 characters long."
    