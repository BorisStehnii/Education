import random

rand_number = random.randint(1, 10)
number = input("Угадай какое число от 1 до 10 я загадал: ")
while True:
    if not number.isdigit():
        number = input("Это не число. Попробуй еще: ")
        continue

    number = int(number)
    if number == rand_number:
        print("Угадал")
        break
    elif number < rand_number:
        number = input("Нет, мое число больше. Попробуй еще: ")
        continue
    else:
        number = input("Нет, мое число меньше. Попробуй еще: ")
        continue
