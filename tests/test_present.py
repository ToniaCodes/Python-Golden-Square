import pytest
from lib.present import * 

def test_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == ("No contents have been wrapped.")
    