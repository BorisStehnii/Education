def sum_func(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    print(sum_)


sum_func(3, 6, 7)
