number_1 = "0500715226"
number_2 = "050071522И"
number_3 = "2333333333333333333"
number = [number_1, number_2, number_3]
i = 0
while i < len(number):
    if number[i].isdigit() and len(number[i]) == 10:
        print(f"{number[i]}: правильный формат")
    else:
        print(f"{number[i]}: Неверный формат")
    i += 1
