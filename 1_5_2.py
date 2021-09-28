Number_1 = "0500715226"
if Number_1.isdigit() and len(Number_1) == 10:
    print(f"{Number_1}: правильный формат")
else:
    print("Не верный формат")

Number_2 = "050071522И"
if Number_2.isdigit() and len(Number_2) == 10:
    print(f"{Number_2}: правильный формат")
else:
    print(f"{Number_2}: Неверный формат")
