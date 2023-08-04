from seasons import check_date
import pytest

def test_check_date():
    assert check_date("2005-02-23") == ["2005","02","23"]
    with pytest.raises(SystemExit):
        assert check_date("July 3, 1998")