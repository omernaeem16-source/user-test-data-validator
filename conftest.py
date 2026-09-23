import json

import pytest


@pytest.fixture
def users():
    with open("data/users.json", "r") as file:
        return json.load(file)