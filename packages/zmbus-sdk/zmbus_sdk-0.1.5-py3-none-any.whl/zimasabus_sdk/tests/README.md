# Zimasabus SDK Tests

This directory contains unit tests for the Zimasabus SDK.

## Running the Tests

To run all tests:

```bash
python -m unittest discover -s zimasabus_sdk/tests
```

To run a specific test file:

```bash
python -m unittest zimasabus_sdk.tests.test_followups
```

## Test Structure

The tests are organized by module:

- `test_followups.py` - Tests for the `FollowUpService` class and related functionality

## Writing New Tests

When writing new tests:

1. Create a new test file named `test_<module_name>.py`
2. Import the necessary classes from the SDK
3. Create a test class that inherits from `unittest.TestCase`
4. Implement test methods that start with `test_`
5. Use mocks to isolate the code being tested from external dependencies
6. Add assertions to verify the expected behavior

## Test Coverage

To generate a test coverage report:

```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run -m unittest discover -s zimasabus_sdk/tests

# Generate report
coverage report -m
``` 