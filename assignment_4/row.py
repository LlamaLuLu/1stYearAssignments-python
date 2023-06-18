# Asks user to enter a number 'n' where -6<n<93 and prints a sequence of 7 numbers starting from n
# Lulama Lingela
# 3 March 2023

start_n = int(input("Enter the start number:\n"))

# numbers printed: field width = 2; right-justified
for n in range(start_n, start_n + 7):
    if n >= 0 and n <= 9:
        print(f" {n}", end=" ")
    else:
        print(n, end=" ")