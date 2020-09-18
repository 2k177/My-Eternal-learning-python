## Intro for Pytest
Change the directory where the pytest file is being placed
Enter pytest in the CLI

### Output for Intro_Pytest.py
```
user-MOBL MINGW64 /c/DS/pytest/Intro_Pytest
$ pytest
==================================================================================================== test session starts =====================================================================================================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: C:\DS\pytest\Intro_Pytest
plugins: pyfakefs-4.1.0, cov-2.10.1
collected 2 items                                                                                                                                                                                                             

test_mathlib.py ..                                                                                                                                                                                                      [100%]

===================================================================================================== 2 passed in 0.59s ======================================================================================================

```
pytest finds the function with test_ as prefix and start executing the function.

