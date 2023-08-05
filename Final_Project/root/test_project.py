from project import is_ValidLink, is_ValidFile, is_ValidOutputName
import pytest

def test_isValidLink():
    assert is_ValidLink("https://www.youtube.com/watch?v=fcZXfoB2f70") == True
    assert is_ValidLink("https://www.youtube.com/watch?v=fJ9rUzIMcZQ") == True
    assert is_ValidLink("https://youtu.be/fcZXfoB2f70") == True
    assert is_ValidLink("https://youtu.be/fJ9rUzIMcZQ") == True
    assert is_ValidLink("https://cs50.harvard.edu/") == False
    assert is_ValidLink("www.google.com") == False
    with pytest.raises(BaseException):
        assert is_ValidLink(123)

def test_isValidFile():
    assert is_ValidFile("input.txt") == True
    assert is_ValidFile("playlist1.txt") == True
    assert is_ValidFile("my_play-list.txt") == True
    assert is_ValidFile("my playlist.txt") == True
    assert is_ValidFile("playlist.png") == False
    assert is_ValidFile("playlist") == False
    with pytest.raises(BaseException):
        assert is_ValidLink(123)

def test_isValidOutput():
    assert is_ValidOutputName("Bohemian Rhapsody - Queen") == True
    assert is_ValidOutputName("Bohemian Rhapsody") == True
    assert is_ValidOutputName("CS50") == True
    assert is_ValidOutputName("CS,50") == False
    with pytest.raises(BaseException):
        assert is_ValidOutputName(123)