# Accepts number n (where -6<n<2) & prints numbers n to n+41 as 6 rows of 7 numbers
# Lulama Lingela
# 11 March 2023

user_num = int(input("Enter a number between -6 and 2:\n"))

counter = 0   # keeps count of iterations per row
if user_num > -6 and user_num < 2:
    for r in range(6):   # creates 6 rows
        for d in range(user_num + 7*r, user_num + 7*(r+1)):   # prints 7 digits per row
            counter += 1
            if counter % 7 != 0 or counter == 0:   # digits requiring space after
                if d >= 0 and d <= 9:
                    print(f" {d}", end=" ")
                else:
                    print(d, end=" ")                                    
            else:   # digits requiring new line after (7th digit)
                if d >= 0 and d <= 9:
                    print(f" {d}")
                else:
                    print(d)                 
            
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")
    