while True:
    height = input("Введите высоту пирамиды в формате '15': ")
    if not height.isdigit():
        print("НЕВЕРНЫЙ формат высоты пирамиды")
    else:
        break
height = int(height)
i = 1
j = height - 1
while i <= (height*2)-1:
    if i > height:
        print(j*"+")
        j -= 1
    else:
        print(i*"+")
    i += 1
