# Accepts name of month & year as input and prints out calendar for that month.
# Lulama Lingela
# 3 April 2023

from math import *

def day_of_week(day, month, year):
    """Returns day of week on which date falls."""
    if month <= 2:
        month += 12
        year -= 1
    day_num = day + floor(13 * (month + 1) / 5) + year + floor(year / 4) - floor(year / 100) + floor(year / 400) % 7
    day_num = (day_num + 5) % 7 + 1
    return day_num


def is_leap(year):
    """Returns True if leap year, False otherwise."""
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def month_num(month_name):
    """Returns month number from 1 to 12."""
    index = 0
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    month_list_l = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if month_name.title() in month_list:
        index = month_list.index(month_name.title())  # identifies index of element in month_list equal to month
    elif month_name.title() in month_list_l:
        index = month_list_l.index(month_name.title())  # identifies index of element in month_list_l equal to month
    return index + 1


def num_days_in(month_num, year):
    """Returns number of days in month."""
    month_30 = [4, 6, 9, 11]
    if month_num == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    elif month_num in month_30:
        return 30
    else:
        return 31


def num_weeks(month_num, year):
    """Returns number of weeks that month spans."""
    day_1 = day_of_week(1, month_num, year)
    days = num_days_in(month_num, year)
    week_count = 1
    for d in range(day_1, days + day_1 - 1):
        if d % 7 == 0 and d != 42:
            week_count += 1
    return week_count


def week(week_num, start_day, days_in_month):
    """Returns string consisting of day of month for each day in week (starting with Monday & ending with Sunday)."""
    week_days = ""
    monday_date = 8 - (start_day - 1) + (week_num - 2) * 7   # own formula to find date of Monday of week
    sunday_date = (8 - start_day) + (week_num - 1) * 7   # own formula to find date of Sunday of week
    if monday_date < 1:   # adds spaces in string for dates before 1st of month
        for i in range(start_day - 1):
            week_days += "   "
        monday_date = 1
    while monday_date <= days_in_month and monday_date <= sunday_date:
        if monday_date < 10:   # single digits with field width of 2, right-justified
            new_day = " " + str(monday_date) + " "
            week_days += new_day
        else:
            new_day = str(monday_date) + " "
            week_days += new_day
        monday_date += 1
    return week_days[:-1]

def main():
    """Obtains name of month & year from user and prints calendar for that month by obtaining number of weeks & week
    string for each."""
    month_name = input("Enter month:\n").title()
    year = eval(input("Enter year:\n"))
    month_n = month_num(month_name)
    week_num = num_weeks(month_n, year)
    start_day = day_of_week(1, month_n, year)
    days_in_month = num_days_in(month_n, year)
    print(month_name)
    print("Mo Tu We Th Fr Sa Su")
    for i in range(1, week_num+1):
        print(week(i, start_day, days_in_month))

if __name__ == '__main__':
    main()
