import sys
import random


string = sys.argv


def phone():
    x = ([str(random.randint(0, 9)) for i in range(10)])
    phone_number = ["+380(", x[0], x[1], x[2], ")", x[3], x[4], x[5], "-", x[6], x[7], "-", x[8], x[9]]
    return phone_number


if len(string) < 2 or string[1].isdigit():
    number = 10
else:
    number = int(string[1])

list_phone_numb = ["".join(phone()) for i in range(number)]
print(list_phone_numb)

input("Press ENTER to exit")
