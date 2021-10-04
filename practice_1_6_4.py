import sys


string = sys.argv
if len(string) < 2:
    print("Введите строку")
    exit(1)

list_str = string[1].lower().split(" ")
dict_words_1 = {}
for key in list_str:
    dict_words_1.update({key: list_str.count(key)})
print("dict_words_1", dict_words_1)

dict_words_2 = {key_2: list_str.count(key_2) for key_2 in list_str}
print("dict_words_2", dict_words_2)
input("Press ENTER to exit")
