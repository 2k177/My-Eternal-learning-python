# Install pytest 
``` python -m pip install pytest ```
## Less Boilerplate
1. Arrange, or set up, the conditions for the test\
2. Act by calling some function or method\
3. Assert that some end condition is true

## Output format:
The output then indicates the status of each test using a syntax similar to unittest:

1. A dot (.) means that the test passed.
2. An F means that the test has failed.
3. An E means that the test raised an unexpected exception.

## Test Filtering
### Name-based filtering:
You can limit pytest to running only those tests whose fully qualified names match a particular expression. You can do this with the -k parameter.
### Directory scoping: 
By default, pytest will run only those tests that are in or under the current directory.
### Test categorization: 
pytest can include or exclude tests from particular categories that you define. You can do this with the -m parameter.
