while True:
    string = input("Введите строку в формате 'abc abcd abc bd abcd':")
    if len(string) == 0:
        print("ВВЕДИТЕ СТРОКУ")
        continue
    break
list_words = string.lower().split(" ")
new_string = {key: list_words.count(key) for key in list_words}
print("Сумма по словам:", new_string)
