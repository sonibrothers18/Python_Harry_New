detail = {
    "name": "harry",
    "marks": 100,
    "list": [1, 2, 9],
    "result": False
}

print(detail.items())
print(detail.keys())
print(detail.values())

detail.update({"name": "mayur", "grade": "college"}) # update name and add grade key
print(detail)

print(detail.get("name")) # give none
print(detail["name"]) # give error