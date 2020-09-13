## Pytest fixture
pytest fixtures are a way of providing data, test doubles, or state setup to your tests. 
Fixtures are functions that can return a wide range of values.
Each test that depends on a fixture must explicitly accept that fixture as an argument.
You can use the fixture by adding it as an argument to your tests.
Its value will be the return value of the fixture function

### Output for Fixture_test.py
```
-MOBL MINGW64 /c/DS/pytest/pytest_Fixture
$ pytest
==================================================================================================== test session starts =====================================================================================================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: C:\DS\pytest\pytest_Fixture
plugins: pyfakefs-4.1.0, cov-2.10.1
collected 2 items                                                                                                                                                                                                             

Fixture_test.py ..                                                                                                                                                                                                      [100%]

===================================================================================================== 2 passed in 0.30s ======================================================================================================

```
