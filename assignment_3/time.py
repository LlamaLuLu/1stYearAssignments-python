# Checks validity of a time entered by user as a set of three integers
# Lulama Lingela
# 24 February 2023

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")