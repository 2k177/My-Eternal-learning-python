import mathlib
import pytest
import sys
@pytest.mark.skip(reason="test not in production")          #Skipping without any condition
def test_calTotal():
    total = mathlib.calTotal(3, 9)
    assert total==12

@pytest.mark.skipif(sys.version_info < (3,5),
                    reason="Old version not allowed")       #Skipping with condition
def test_calMultiply():
    result = mathlib.calMultiply(10, 8)
    assert result==80

def test_dummy():                                           #execute "py.test -k dummy" to get dummy test alone passed(Name filtering)
    assert True

@pytest.mark.windows                                        #Test Categorization
def test_windows_1():                                       #pytest -m windows -v --> to get the tests under windows
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True
@pytest.mark.mac
def test_mac_2():
    assert True