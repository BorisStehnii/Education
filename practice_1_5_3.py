import sys


string = sys.argv

if len(string) != 2:
    print("Введите строку в формате: 'тут могло быть Ваме имя'")
    input("Press ENTER to exit")    # удержание консольного окна
    exit(1)
string = string[1]

li_1 = string.split(" ")
new_li = li_1[::-1]
print("Строка:", li_1)
print("Строка в обратную сторону:", new_li)
input("Press ENTER to exit")
