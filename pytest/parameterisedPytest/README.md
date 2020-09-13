## Parametrization: Combining Tests

parametrize a single test definition, and pytest will create variants of the test for you with the parameters you specify.

## parameterisedPytest
```

userx-MOBL MINGW64 /c/DS/pytest/parameterisedPytest
$ pytest
==================================================================================================== test session starts =====================================================================================================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: C:\DS\pytest\parameterisedPytest
plugins: pyfakefs-4.1.0, cov-2.10.1
collected 4 items                                                                                                                                                                                                             

test_mathlib.py ....                                                                                                                                                                                                    [100%]

===================================================================================================== 4 passed in 0.18s ======================================================================================================

```
It is useful for passing multiply input for same funtion.
