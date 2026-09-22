import json
import pytest


# Approach 1
# The below fixture is only providing data to the test function in test_validator

@pytest.fixture()
def users():
    with open("data/users.json", "r") as file:
      data = json.load(file)
      return data

    # jab bhi fixture call karenge test function mein tou loop mein fixture ka name he use karenge



 # Approach 2
