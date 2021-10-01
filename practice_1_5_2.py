import sys


string = sys.argv

string_low = string[1].lower()
string_set = list(set(string_low))
new_string = []
i = 0
while i < len(string_set):
    new_string.append((string_set[i], string_low.count(string_set[i])))
    i += 1
print("new_string:", new_string)

input("Press ENTER to exit")
