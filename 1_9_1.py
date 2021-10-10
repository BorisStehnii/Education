with open("myfile.txt", "a") as file:
    file.write("Hello file world!\n")

with open("myfile.txt") as file:
    print(file.read())


input("Enter")
