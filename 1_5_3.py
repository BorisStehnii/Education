name_saved = "борис"
i = 0
while True:
    i += 1
    name_keyboard = input("Введите имя и нажмите Enter: ")
    if name_keyboard.lower() == name_saved:
        print("Имя принято")
        break
    elif i == 1:
        print("Имя не верно. Осталось две попытки!")
    elif i == 2:
        print("Имя не верно. Осталась одна попытка!")
    else:
        print('Имя не верно.')
        break
