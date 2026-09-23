import json


with open("data/users.json", "r") as file:
    data = json.load(file)

print(data)