import time


day = time.strftime("%A")
name = "Creator"      # задаем имя

print(f"Good day {name}! {day} is a perfect day to learn some python.")     # применяем f

print("Good day %s! %s is a perfect day to learn some python." % (name, day))      # применяем %

print("Good day {}! {} is a perfect day to learn some python.".format(name, day))       # применяем format
