a = input("Введи а: ")
b = input("Ввуди b: ")
try:

    d = int(a)**2/int(b)
    print(d)
except ValueError:
    print("ValueError")
    exit(1)
except ZeroDivisionError:
    print("ZeroDivisionError")
    exit(1)