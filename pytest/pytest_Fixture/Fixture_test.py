import pytest

@pytest.fixture
def targetValue():
    input = 39
    return input

def test_mod_10(targetValue):
    assert targetValue % 10 == 9

def test_mul_10(targetValue):
    assert targetValue * 10 == 390