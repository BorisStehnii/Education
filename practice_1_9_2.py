def func_(str_, symbol="."):
    str_new = " ".join(str_.lower().split())
    if str_new[-1] != symbol:
        str_new += symbol
    return str_new


print(func_("aD  sd", "/"))
