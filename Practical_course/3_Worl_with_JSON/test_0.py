import json

json1 = {
    "name": "Petya",
    "age": 23,
    "sex": True,
    "languages": [{"Python": 9}, {"Java": 7}, {"C#": 8}],
    "pc": {"os": "Linux", "proc": "Intel Core i7-8700", "ram": 64, "hard": 5000}
}

s = json.dumps(json1, indent=2)
print(s)
with open("file.json", "w") as json_file:
    json.dump(json1, json_file, indent=2)

s = json.dumps(json1)

json2 = json.loads(s)

if json1 == json2:
    print('+')

with open("file.json", "r") as json_file:
    json2 = json.load(json_file)

print(json2)
