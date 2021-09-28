x = []
z = []
i = 1
while i <= 100:
    x.append(i)
    if x[i-1] % 7 == 0 and x[i-1] % 5 > 0:
        z.append(i)
    i += 1
print("Список с числами от 1 до 100:", x)
print("Числа кратные 7 но не кратные 5:", z)
