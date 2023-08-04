from plates import is_valid

def test_req1():
    assert is_valid("A123") == False
    assert is_valid("CS123") == True

def test_req2():
    assert is_valid("S") == False
    assert is_valid("1") == False   
    assert is_valid("ASD1234") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS50") == True
    assert is_valid("CS1234") == True

def test_req3():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA012") == False
    assert is_valid("AAA222") == True

def test_req4():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False   
    assert is_valid("CS:50") == False     