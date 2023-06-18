# Transforms date & time in compact 24hr format to long 12hr format
# Lulama Lingela
# 18 March 2023

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

user_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")
# shortens year
year = "'" + user_time[2:4]
# identifies month in words
month_i = int(user_time[5:7]) - 1
month = month_list[month_i]
# identifies day & adds suffix
day = user_time[8:10]
day_z = int(day[-1])
if int(day) == 11:
    day = f"{int(day)}th"
elif day_z == 1:
    day = f"{int(day)}st"
elif day_z == 2:
    day = f"{int(day)}nd"
elif day_z == 3:
    day = f"{int(day)}rd"
else:
    day = f"{int(day)}th"
# converts time: digital to analogue
hr = int(user_time[11:13])
if hr == 0:
    time = f"12:{user_time[14:16]} am"
elif 0 < hr < 12:
    time = f"{hr}:{user_time[14:16]} am"
elif hr == 12:
    time = f"{hr}:{user_time[14:16]} pm"
else:
    hr -= 12
    time = f"{hr}:{user_time[14:16]} pm"

final = f"{time} on the {day} of {month} {year}"
print(final)