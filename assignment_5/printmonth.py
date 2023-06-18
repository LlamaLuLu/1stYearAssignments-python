# Asks the user for a month name and start day and then prints the calendar for that month in a 6 row by 7 column grid
# Lulama Lingela
# 11 March 2023

# database of months
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_list_l = ["jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sep", "oct", "nov", "dec"]
month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

month = input("Enter the name of a month (e.g. January, ..., December):\n")
day = int(input("Enter the start day (1 for Monday, ..., 7 for Sunday):\n"))

if (month in month_list or month in month_list_l) and (1 <= day <= 7):
    if month in month_list:
        index = month_list.index(month)  # identifies index of element in month_list equal to user input
    elif month in month_list_l:
        index = month_list_l.index(month)  # identifies index of element in month_list_l equal to user input
    print(f"{month_list[index]}\nMo Tu We Th Fr Sa Su")

    month = month_list[index]
    counter = 0   # keeps count of iterations per row
    position = day * (-1) + 2   # shifts first day of month

    month_counter = 1   # assigns no. of days to each month
    while month_counter != index + 1:
        month_counter += 1
    if month_counter == 2 and day == 1:  # special case for Feb
        print()
    for r in range(6):   # creates 6 rows
        for d in range(position + 7*r, position + 7*(r+1)):   # prints 7 digits per row
            counter += 1
            if counter % 7 != 0 or counter == 0:   # digits requiring space after
                if month_counter == 2 and (d < 1 or d > 28):   # changes range of days based on month
                    print("  ", end=" ")
                elif month_counter in month_30 and (d < 1 or d > 30):
                    print("  ", end=" ")
                elif month_counter in month_31 and (d < 1 or d > 31):
                    print("  ", end=" ")
                elif 0 <= d <= 9:   # digits for general case
                    print(f" {d}", end=" ")
                else:
                    print(d, end=" ")  
            else:   # digits requiring new line after (7th digit)
                if month_counter == 2 and (d < 1 or d > 28):   # changes range of days based on month
                    print("  ")
                elif month_counter in month_30 and (d < 1 or d > 30):
                    print("  ")
                elif month_counter in month_31 and (d < 1 or d > 31):
                    print("  ")
                elif 0 <= d <= 9:   # digits for general case
                    print(f" {d}")
                else:
                    print(d)
else:
    print("Invalid calendar: you have either entered an incorrect month name or start day.")