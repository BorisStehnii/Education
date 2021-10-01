import sys


string = sys.argv

if len(string) != 2 or string[1].isdigit() is False:
    print("Введите число формата: '345'")
    input("Press ENTER to exit")    # удержание консольного окна
    exit(1)

string = string[1]
sum_number = 0
i = 0
while i < len(string):
    sum_number += int(string[i])
    i += 1
print("Сумма цифр в строке:", sum_number)

input("Press ENTER to exit")
