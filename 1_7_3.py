import random

string_ = input("Введи строку")
string_new = "".join(string_.split(" "))
number_ = list(range(len(string_new)))
set_words = set()
while True:
    random.shuffle(number_)
    set_words.add("".join(string_new[i] for i in number_))
    if len(set_words) == 5:
        break
print(set_words)
