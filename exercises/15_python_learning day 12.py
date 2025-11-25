import datetime
current_hour = datetime.datetime.now() .hour
current_minute = datetime.datetime.now() .minute
current_seconds = datetime.datetime.now() .second
print(f"The current time is: {current_hour:02}:{current_minute:02}:{current_seconds:02}")
if current_hour >= 5 and current_hour < 12:
    print("good morning sir")
elif current_hour >= 12 and current_hour < 16:
    print("good after noon sir")
elif current_hour >= 16 and current_hour < 19:
    print("good evening sir")
else:
    (print("good night sir"))

#if current_hour >= 5 and current_hour < 12: #IF WE DONT WANT FOR IF CONDITIONS NOT HAVING PARATHISIS IS ASO OK
#     print("good morning sir")
# elif current_hour >= 12 and current_hour < 16:
#     print("good after noon sir")
# elif current_hour >= 16 and current_hour < 19:
#     print("good evening sir")
# else:
#     (print("good night sir"))
# so basically while writing  the condition for if statment, feel free to remove the parathisis, as its standered python style. if u see them they are probaly just for clarity or old habbits
# whre can use it