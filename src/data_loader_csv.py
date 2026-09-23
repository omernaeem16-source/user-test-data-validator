import csv


with open("data/users.csv", "r") as file:
    data = csv.DictReader(file)
    users = list(data)


for user in users:
    user["id"] = int(user["id"])
    user["age"] = int(user["age"])

    if user["active"] == "True":
        user["active"] = True
    elif user["active"] == "False":
        user["active"] = False

print(users)