# Добавил eval
import random

while True:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    oper_1 = random.choice(["-", "+", "*"])
    oper_2 = random.choice(["-", "+", "*"])

    while True:
        result = input(f"{x} {oper_1} {x} {oper_2} {y} = ")
        if not result.replace("-", "").isdigit():
            continue
        elif int(result) == eval(f"{x} {oper_1} {x} {oper_2} {y}"):
            print("Right")
            break

    command = input("will we continue?(Y/n):")
    if command.lower() == "y":
        continue
    else:
        break
