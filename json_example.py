import json

json_data = '{"name": "", "age": 25}'
parsed_data = json.loads(json_data)
print(parsed_data)

data = {
    "name": "John",
    "age": 25
}
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_exemple.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data)

    with open("json_user.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)