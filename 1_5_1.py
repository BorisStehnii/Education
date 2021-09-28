# string_1 > 2
string_1 = "abeeecd"
print("string_1", string_1)
if len(string_1) >= 2:
    string_2 = string_1[0:2] + string_1[-2:]
else:
    string_2 = string_1
print("string_2", string_2, "\n" + 15*"_")

# string_1 = 2
string_1 = "ab"
print("string_1", string_1)
if len(string_1) >= 2:
    string_2 = string_1[0:2] + string_1[-2:]
else:
    string_2 = string_1
print("string_2", string_2, "\n" + 15*"_")

# string_1 < 2
string_1 = "a"
print("string_1", string_1)
if len(string_1) >= 2:
    string_2 = string_1[0:2] + string_1[-2:]
else:
    string_2 = string_1
print("string_2", string_2, "\n" + 15*"_")
