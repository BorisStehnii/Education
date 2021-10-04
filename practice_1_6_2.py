import sys


params = sys.argv
if len(params) != 2:
    print("Введите строку")
    exit(1)

string = params[1].lower()
res_dict = {}
# способ 1
for l in string:
    if l in res_dict:
        res_dict[l] += 1
    else:
        res_dict[l] = 1
# способ 2 в одну строку 
res_dict = {l: string.count(l) for l in string}

print(res_dict)

input("Press ENTER to exit")
