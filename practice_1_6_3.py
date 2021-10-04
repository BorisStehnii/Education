inform_user = ["name", "age", "city"]
dict_user = {}
for key in inform_user:
    dict_user[key] = input(f"Type your {key}:")
    if key == "age" and dict_user[key].isdigit():
        dict_user[key] = int(dict_user[key])
    elif key == "age" and not dict_user[key].isdigit():
        print("Incorrect format 'age'")
        exit(1)
print(dict_user)
