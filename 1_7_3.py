# Сократил код
import random

string_ = input("Введи строку")
words_ = list(string_.replace(" ", ""))
set_words = set()
while len(set_words) < 5:
    random.shuffle(words_)
    set_words.add("".join(words_))
print(set_words)
