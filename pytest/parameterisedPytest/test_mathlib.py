import mathlib
import pytest
# import numpy

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5,25),
                             (3,9),
                             (10,100)

                         ])
def test_calc_square(test_input , expected_output):
    result = mathlib.square(test_input)
    assert result == expected_output

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             ((5,5),25),

                         ])
def test_calMultiply(test_input , expected_output):
    print(test_input)
    result = 1
    for x in test_input:
        result *=x

    assert result == expected_output
