import random


i = 0
li_numbers = []
while i <= 10:
    li_numbers.append(random.randint(0, 100))
    i += 1
print("Список:", li_numbers)
print("Максимальное:", max(li_numbers))
