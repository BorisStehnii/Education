name = input("What is your name?: ")
years = input("How old are you?: ")
while True:
    if not years.isdigit():
        years = input("Enter the number. How old are you?: ")
        continue
    break
print("Hello", name, ", on your next birthday you’ll be", int(years) + 1, "years")
