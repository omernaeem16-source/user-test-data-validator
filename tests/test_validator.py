import json
import pytest

from validator import validate_user, validate_age


with open("data/users.json", "r") as file:
    users = json.load(file)


expected_results = [True, True, False, False, False, False]

expected_errors = {
    101: [],
    102: [],
    103: ["Name is empty"],
    104: ["Invalid email"],
    105: ["Invalid age"],
    106: ["Invalid Active"]
}


@pytest.mark.parametrize(
    "user, expected",
    list(zip(users, expected_results))
)
def test_user(user, expected):
    result = validate_user(user)

    assert result["valid"] == expected
    assert result["errors"] == expected_errors[user["id"]]


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (100, True),
        (101, False)
    ]
)
def test_age_boundaries(age, expected):
    result = validate_age(age)

    assert result["valid"] == expected


def test_invalid_id_zero():
    user = {
        "id": 0,
        "name": "Omer",
        "email": "omer@example.com",
        "age": 28,
        "active": True
    }

    result = validate_user(user)

    assert result["valid"] is False
    assert result["errors"] == ["Invalid ID"]


def test_invalid_id_negative():
    user = {
        "id": -5,
        "name": "Omer",
        "email": "omer@example.com",
        "age": 28,
        "active": True
    }

    result = validate_user(user)

    assert result["valid"] is False
    assert result["errors"] == ["Invalid ID"]


def test_invalid_active_type():
    user = {
        "id": 107,
        "name": "Omer",
        "email": "omer@example.com",
        "age": 28,
        "active": "yes"
    }

    result = validate_user(user)

    assert result["valid"] is False
    assert result["errors"] == ["Invalid Active"]