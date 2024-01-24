import json

with open('data/kabum/departamentos.json', 'r') as file:
    data = json.load(file)

for item in data:
    print(item["name"], item["parameter"])
