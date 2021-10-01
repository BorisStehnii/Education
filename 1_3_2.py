import random


li_1 = []
li_2 = []
new_li_1 = []
new_li_2 = []
i = 0
while i <= 9:
    li_1.append(random.randint(1, 10))
    li_2.append(random.randint(1, 10))
    i += 1
print("Список Первый:", li_1)
print("Список Второй:", li_2)

# №1 поиск совместных элементов через пересечение множеств
new_li_1 = sorted(list(set(li_1) & set(li_2)))
print("Список совместных элементов через пересечение:", new_li_1)

# №2 поиск совместных элементов через цикл
li_1 = list(set(li_1))
i = 0
while i < len(li_1):
    if li_1[i] in li_2:
        new_li_2.append(li_1[i])
    i += 1
print("Список совместных элементов через цикл:", new_li_2)
