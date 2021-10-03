import sys


params = sys.argv
if len(params) != 3 or not params[1].isdigit():
    print("Введите число и символ для построения пирамиды '13' '&'")
    exit(1)
height = int(params[1])
symbol_ = params[2]

# while True:
#     height = input("Введите высоту пирамиды в формате '15': ")
#     symbol_ = input("Введите символ пирамиды в формате '*': ")
#     if not height.isdigit():
#         print("НЕВЕРНЫЙ формат высоты пирамиды")
#     else:
#         break


j = height - 1
for i in range(height*2):
    if i > height:
        print(j * f"{symbol_}")
        j -= 1
    else:
        print(i * f"{symbol_}")
    i += 1

input("Press ENTER to exit")
