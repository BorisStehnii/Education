import sys
import random


string = sys.argv


def phone():
    phone_number = ["+380(" + str(random.randint(100, 999)) + ")" + str(random.randint(100, 999)),
                    "-" + str(random.randint(10, 99)) + "-" + str(random.randint(10, 99))]
    return phone_number


if len(string) < 2 or string[1].isdigit():
    number = 10
else:
    number = int(string[1])

list_phone_numb = ["".join(phone()) for _ in range(number)]
print(list_phone_numb)

input("Press ENTER to exit")
