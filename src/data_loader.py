import json
from validator import validate_user

with open("data/users.json", "r") as file:
    data = json.load(file)

print(data)

