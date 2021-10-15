def error_oops():
    a = [1, 2]
    print(a[3])


def check_error_oops_1():
    try:
        error_oops()
    except IndexError:
        print("IndexError")


def check_error_oops_2():
    try:
        error_oops()
    except KeyError:
        print("IndexError")


check_error_oops_1()
check_error_oops_2()
