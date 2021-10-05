while True:
    string = input("Введите строку в формате 'abc abcd abc bd abcd':")
    if len(string) == 0:
        print("ВВЕДИТЕ СТРОКУ")
        continue
    break
list_words = string.lower().split()
set_list_words = set(list_words)
new_dict = {key: list_words.count(key) for key in set_list_words}
print("Сумма по словам:", new_dict)
