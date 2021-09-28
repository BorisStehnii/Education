Number_1 = "0500715226"
Number_2 = "050071522И"
Number = [Number_1, Number_2]
i = 0
while i < 2:
    if Number[i].isdigit() and len(Number_2) == 10:
        print(f"{Number[i]}: правильный формат")
    else:
        print(f"{Number[i]}: Неверный формат")
    i += 1
