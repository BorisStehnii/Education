str_1 = "today is the python day"
print("Строка_1:", str_1)
# через .title
str_2 = str_1.title()
print("Строка_2:", str_2)
# через цикл while
str_3 = []
str_1 = str_1.split(" ")
i = 0
while i <= len(str_1)-1:
    str_3.append(str_1[i].capitalize())
    i += 1
str_3 = " ".join(str_3)
print("Строка_3:", str_3)
