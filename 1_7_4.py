import random

while True:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    result = input(f"{x} + {x} * {y} = ")
    while True:
        if int(result) == (x + x*y):
            print("Right")
            break
        else:
            result = input(f"{x} + {x} * {y} = ")
            continue
    command = input("will we continue?(Y/n):")
    if command.lower() == "y":
        continue
    else:
        break
