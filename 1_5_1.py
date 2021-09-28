string_1 = "abeeecd"
string_2 = "ab"
string_3 = "a"
strings = [string_1, string_2, string_3]
i = 0
while i < len(strings):
    print("string", strings[i])
    string = strings[i]
    if len(strings[i]) >= 2:
        string = string[0:2] + string[-2:]
    print("new string", string, "\n" + 15 * "_")
    i += 1
