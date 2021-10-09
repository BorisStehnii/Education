import sys


string_ = sys.argv[1]


with open("task_3.txt", "a+") as file_:
    file_.write(string_ + "\n")

with open("task_3.txt") as file_:
    text_ = file_.readline()

print(text_)
print()

input("Enter")
