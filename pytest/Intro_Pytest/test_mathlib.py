import mathlib

def test_calTotal():
    total = mathlib.calTotal(3, 9)
    assert total==12
def test_calMultiply():
    result = mathlib.calMultiply(10, 8)
    assert result==80