import random

x = []
y = []
z_1 = []
z_2 = []
i = 0
while i <= 9:
    x.append(random.randint(1, 10))
    y.append(random.randint(1, 10))
    i += 1
print("Список x:", x)
print("Список y:", y)

# №1 поиск совместных элементов через пересечение множеств
z_1 = sorted(list(set(x) & set(y)))
print("Список совместных элементов через пересечение", z_1)
# №2 поиск совместных элементов через цикл
x = list(set(x))
i = 0
while i < len(x):
    if x[i] in y:
        z_2.append(x[i])
    i += 1
print("Список совместных элементов через цикл", z_2)
