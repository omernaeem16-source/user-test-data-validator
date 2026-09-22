import csv

with open("data/users.csv", "r") as file:
    data = csv.DictReader(file)

    users=list(data)
    print(users)

for user in users:
   user["id"] = int(user["id"])
   user["age"] = int(user["age"])
   user["active"] = user["active"] == "True"

print(users)