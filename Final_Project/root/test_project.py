from project import is_ValidLink
import pytest

def test_isValidLink():
    assert is_ValidLink("https://www.youtube.com/watch?v=fcZXfoB2f70") == True
    assert is_ValidLink("https://www.youtube.com/watch?v=fJ9rUzIMcZQ") == True
    assert is_ValidLink("https://youtu.be/fcZXfoB2f70") == True
    assert is_ValidLink("https://youtu.be/fJ9rUzIMcZQ") == True
    assert is_ValidLink("https://cs50.harvard.edu/") == False
    assert is_ValidLink("www.google.com") == False
    with pytest(BaseException):
        assert is_ValidLink(123)