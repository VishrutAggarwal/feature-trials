import json

hello = {
        "schemaVersion": 1,
        "label": "Hello",
        "message": "World",
        "color": "green"
        }
f = open("myjsonfile.json", "w")

json_object = json.dumps(hello, indent=2)
f.write(json_object)