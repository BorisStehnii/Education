import random

i = 0
x = []
while i <= 10:
    x.append(random.randint(0, 100))
    i += 1
print("Список:", x)
print("Максимальное:", max(x))
