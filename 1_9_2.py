import json


def exit_():
    command_1 = input("Выход(Е/n): ")
    if command_1.lower() == "e":
        exit(0)


def add_new():

    while True:
        telephone_number = input("введи номер телефона:").lower()
        if telephone_number.isdigit():
            break

    first_name = input("введи новое имя:").lower()
    last_name = input("введи новую фамилию:").lower()
    city = input("введи новый город:").lower()
    full_name = first_name + " " + last_name
    entries = {telephone_number: {"first": first_name,
                                  "last": last_name,
                                  "full": full_name,
                                  "city": city}}
    with open("Phonebook.json", "r") as phonebook:
        data = json.load(phonebook)
    data.update(entries)
    with open("Phonebook.json", "w+") as phonebook:
        json.dump(data, phonebook)


def search():
    search_by = input("Введите для поиска: ").lower()
    with open("Phonebook.json", "r") as phonebook:
        data_1 = json.load(phonebook)
        for key_1 in data_1:
            if key_1 == search_by:
                print(key_1, data_1[key_1])
                break
            data_2 = data_1[key_1]
            for value in data_2.values():
                if value == search_by:
                    print(key_1, data_1[key_1])
                    break


def delete():
    key = input("Введите номер телефона")
    with open("Phonebook.json", "r") as phonebook:
        data = json.load(phonebook)
    if data.get(key):
        del data[key]
    else:
        print("нет такого номера")
    with open("Phonebook.json", "w+") as phonebook:
        json.dump(data, phonebook)


def command():
    command_ = input("Какое действие ты хочешь сделать (запись-А, поиск-S, обновление для номера-U, удаление-D, "
                     "выход-Е: ")
    if command_.lower() == "a":
        add_new()
    elif command_.lower() == "s":
        search()
    elif command_.lower() == "u":
        add_new()
    elif command_.lower() == "d":
        delete()
    exit_()


while True:
    command()
