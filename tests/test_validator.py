import pytest
import json
from validator import validate_user, validate_id, validate_age
 # Approach 1
# Below code tests all the users in a single test function as a single test case.

code_text=""""

def test_all_users(users):
    expected = {
        101: {"valid": True, "errors": []},
        102: {"valid": True, "errors": []},
        103: {"valid": False, "errors": ["Name is empty"]},
        104: {"valid": False, "errors": ["Invalid email"]},
         105: {"valid": False, "errors": ["Invalid age"]},
         106: {"valid": False, "errors": ["Invalid Active"]}
   }

    for all_users in users:
        expected_result = expected[all_users["id"]]
        result = validate_user(all_users)
        assert result["valid"] == expected_result["valid"]
        assert result["errors"] == expected_result["errors"]

        """

# Below code tests every user as a single test case

   
# Approach 2

code_text=""""

import pytest
import json
from validator import validate_user

with open("data/users.json", "r") as file:
    users = json.load(file)
    expected = [True, True, False, False, False, False]

    print(list(zip(users, expected))) # Just for understanding

    expected_errors = {
    101: [],
    102: [],
    103: ["Name is empty"],
    104: ["Invalid email"],
    105: ["Invalid age"],
    106: ["Invalid Active"]
}

@pytest.mark.parametrize("user, expected", list(zip(users, expected)))
def test_user(user, expected):
    result = validate_user(user)
    print(result)
    assert result["valid"] == expected
    assert result["errors"]== expected_errors[user["id"]]

       """

# Use of zip to create a list of users and expected valid with their corresponsidng values.


# Used edge-case to validate age
@pytest.mark.parametrize("age, expected", [
    (17, False),
    (18, True),
    (100, True),
    (101, False)
])
def test_age_boundaries(age, expected):
    result = validate_age(age)

    assert result["valid"] == expected