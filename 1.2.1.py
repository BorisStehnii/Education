import datetime

# определяем день недели)
day = datetime.datetime.today()
day = day.weekday()
if day == 0:
    day = "Monday"
elif day == 1:
    day = "Tuesday"
elif day == 2:
    day = "Wednesday"
elif day == 3:
    day = "Thursday"
elif day == 4:
    day = "Friday"
elif day == 5:
    day = "Saturday"
else:
    day = "Sunday"
# задаем имя
name = "Our Maker"
# применяем f
print(f"Good day {name}! {day} is a perfect day to learn some python.")
# применяем %
print(f"Good day %s! %s is a perfect day to learn some python." % (name, day))
# применяем format
print("Good day {}! {} is a perfect day to learn some python.".format(name, day))
