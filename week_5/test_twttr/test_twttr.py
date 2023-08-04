from twttr import shorten


def test_single():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"


def test_multi():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_vowel():
    assert shorten("euo") == ""
    assert shorten("EUO") == ""


def test_no_vowel():
    assert shorten("dry") == "dry"
    assert shorten("DRY") == "DRY"


def test_number():
    assert shorten("123") == "123"
    assert shorten("2302") == "2302"


def test_punction():
    assert shorten("Hello!") == "Hll!"
