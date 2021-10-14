with open("myfile.txt", "a") as file:
    file.write("Hello file world!\n")

with open("myfile.txt") as file:
    for i in range(5):
        print(file.readline())


input("Enter")
