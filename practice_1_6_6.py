import sys


string = sys.argv
if len(string) < 2:
    print("Введите название страны или города")
    exit(1)
name = string[1].lower()
dict_country = {"швеция": "стокгольм", "украина": "киев", "испания": "мадрид", "англия": "лондон", "германия": "берлин"}
titl = 0
for key, word in dict_country.items():
    if key == name:
        titl = word.title()
    elif word == name:
        titl = key.title()

if titl == 0:
    titl = "Not found"
print(titl)

input("Press ENTER to exit")
