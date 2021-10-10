def make_country(oper_, *args):
    if oper_ != "-" and oper_ != "+" and oper_ != "*":
        exit(1)
    elif not "".join(map(str, args)).replace("-", "").isdigit():
        exit(1)

    string_ = oper_.join(map(str, args))
    result = eval(string_)
    print(string_, "=", result)


make_country("+", 7, -8, 9)
make_country("-", 8, 5, 3, -10)
make_country("*", 4, 3, -15)
