import json

student = {
    "name": "Diwas",
    "age": 22
}
with open("ice_Cream.json", "w") as file:
    json.dump(student, file)

with open("ice_Cream.json", "r") as file:
    data = json.load(file)
    data.update({"grade": 22})
with open("ice_Cream.json", "w") as file:
    json.dump(data, file)