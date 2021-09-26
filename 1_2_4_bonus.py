name = "Creator"
weather = "sunny"
message_1 = f"Hey {name}, is it {weather} today"
print(message_1)
message_2 = "Hey " + name + ", is it " + weather + " today"
print(message_2)
message_3 = "Hey {1}, is it {0} today".format(weather, name)
print(message_3)
message_4 = "Hey %s, is it %s today" % (name, weather)
print(message_4)
