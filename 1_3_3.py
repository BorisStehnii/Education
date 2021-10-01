li_numbers = []
new_li_numbers = []
i = 1
while i <= 100:
    li_numbers.append(i)
    if li_numbers[i-1] % 7 == 0 and li_numbers[i-1] % 5 > 0:
        new_li_numbers.append(i)
    i += 1
print("Список с числами от 1 до 100:", li_numbers)
print("Числа кратные 7 но не кратные 5:", new_li_numbers)
