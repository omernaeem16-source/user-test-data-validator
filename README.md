# User Test Data Validator

## Project Overview

This project validates user test data loaded from JSON and CSV files.

It checks:

* User ID
* Name
* Email
* Age
* Active status

The project uses Python and PyTest to perform automated validation and data-driven testing.

## Technologies Used

* Python
* PyTest
* JSON
* CSV
* PyTest Fixtures
* PyTest Parametrization
* PyTest Markers

## Project Structure

```text
user_test_data_validator/
│
├── data/
│   ├── users.json
│   └── users.csv
│
├── src/
│   ├── validator.py
│   ├── data_loader.py
│   ├── data_loader_csv.py
│   └── __init__.py
│
├── tests/
│   ├── test_validator.py
│   └── test_csv_validator.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Validation Rules

| Field  | Validation Rule                       |
| ------ | ------------------------------------- |
| ID     | Must be a positive integer            |
| Name   | Must not be empty                     |
| Email  | Must contain `@`                      |
| Age    | Must be between 18 and 100            |
| Active | Must be a boolean (`True` or `False`) |

## Running Tests

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest -c .\pytest.ini -v
```

Run tests with detailed output:

```bash
pytest -c .\pytest.ini -v -s
```

Run regression tests:

```bash
pytest -c .\pytest.ini -m regression -v
```

## Test Coverage

The project includes automated tests for:

* JSON user data validation
* CSV user data validation
* Valid and invalid user data
* ID validation
* Name validation
* Email validation
* Age boundary testing
* Active status type validation
* PyTest parametrization
* PyTest fixtures
* PyTest markers
* Negative testing
* Edge-case testing
* Data-driven testing

## Test Data

The project contains both JSON and CSV datasets with valid and intentionally invalid user records.

The test suite verifies that invalid records are correctly identified and that the expected validation errors are returned.

## PyTest Features Demonstrated

This project demonstrates practical usage of:

* Fixtures
* Fixture dependency
* Parametrization
* Custom markers
* Regression test selection
* Assertions
* Negative testing
* Edge-case testing
* Data-driven testing

## Purpose

This project was created as a practical QA Automation project to demonstrate Python and PyTest skills through automated validation of structured test data.

