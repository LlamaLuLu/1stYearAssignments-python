# Prints every 7th number in range n to n+41, starting from user input
# Lulama Lingela
# 5 March 2023

user_n = int(input("Enter a number:\n"))

for n in range(user_n, user_n + 41, 7):
    if n >= 0 and n <= 9:
        print(f" {n}")
    else:
        print(n)    
