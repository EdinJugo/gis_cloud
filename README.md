# GIS Cloud assignment

This is a test suite for automated login tests on the GIS Cloud Editor web application. The tests are written in Python using the Selenium WebDriver framework.

## Prerequisites

Before running the tests, ensure you have the following prerequisites:

- Python 3
- Selenium WebDriver
- Firefox WebDriver
- Python `unittest` module

## Setup

1. **Python 3**: Make sure you have Python 3 installed.

2. **Selenium WebDriver**: Install the Selenium WebDriver library using pip:

   ```bash
   pip install selenium
   ```

## Running the Tests

To run the test suite, execute the following command:

   ```bash
   python test_login.py
   ```

## Test Cases
1. Test Successful Login

    Test case: test_login_success \
    Description: Test a successful login by entering valid credentials and verifying the result.

2. Test Failed Login

    Test case: test_login_failed  \
    Description: Test a failed login by entering incorrect credentials and verifying the error message.

## Test Results

Successful login will verify that the page loads correctly with the "Create New Map" button.  \
Failed login will verify the error message "Username or password is incorrect."