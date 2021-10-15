a = input("Введи а: ")
b = input("Ввуди b: ")
try:
    d = a**2/b
    print(d)
except TypeError:
    exit(1)
