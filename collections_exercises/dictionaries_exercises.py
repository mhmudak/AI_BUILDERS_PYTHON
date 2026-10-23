# Dictionary: ordered, changeable, do not allow duplicates
#select an item by key, update

my_dict = {
    "name": "mhmud",
    "age": "31",
    "age": "30"
}

print(my_dict)
print(type(my_dict))
print(len(my_dict))

#accessing items
print(my_dict["name"])
print(my_dict["age"])

new_dict = {
    "name": "mhmud",
    "age": "31",
    "age": "30",
    "colors": ["red", "blue", "green"],
    "cars": {"BMW", "JEEP"}
}
print(new_dict)

my_dict["name"]="steve"
print(my_dict)

my_dict.update({"city": "Dusseldorf"})
print(my_dict)

my_dict.update({"city": "Mannheim"})
print(my_dict)

my_dict["city"] = "Munchen"
print(my_dict)

my_dict["country"]="Germany"
print(my_dict)

my_dict.pop("age")
print(my_dict)

del my_dict["city"]
print(my_dict)

my_dict.clear()
print(my_dict)