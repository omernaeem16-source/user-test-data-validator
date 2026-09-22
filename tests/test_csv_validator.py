import csv
import pytest
from validator import validate_user

with open("data/users.csv", "r") as file:
    data = csv.DictReader(file)
    users = list(data)

    

for user in users:
    user["id"] = int(user["id"]) # converts string to integer
    user["age"] = int(user["age"]) # converts string to integer

    if user["active"] == "True":  # converts string to boolean
        user["active"] = True
    elif user["active"] == "False":
        user["active"] = False
    print(user)


expected = [True, True, False, False, False, False]
expected_errors = {
    101: [],
    102: [],
    103: ["Name is empty"],
    104: ["Invalid email"],
    105: ["Invalid age"],
    106: ["Invalid Active"]
}

@pytest.mark.regression
@pytest.mark.parametrize("user, expected", list(zip(users, expected)))
def test_csv_user(user, expected):
    result = validate_user(user)
    print(result)
    assert result["valid"] == expected
    assert result["errors"]== expected_errors[user["id"]]


