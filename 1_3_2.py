import random

x = []
y = []
z = []
i = 0
while i <= 9:
    x.append(random.randint(1, 10))
    y.append(random.randint(1, 10))
    i += 1
print("Список x:", x)
print("Список y:", y)
i = 0
while i <= len(x)-1:
    if x.count(x[i]) > 1:
        x.remove(x[i])
        i -= 1
    i += 1
i = 0
while i <= len(x)-1:
    if x[i] in y:
        z.append(x[i])
    i += 1
print("Список совместных элементов", z)