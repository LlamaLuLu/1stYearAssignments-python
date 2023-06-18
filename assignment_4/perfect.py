# To determine if a given number is a perfect number or not
# Lulama Lingela
# 2 March 2023

number = int(input("Enter a number:\n"))

print(f"The proper divisors of {number} are:")
sum = 0
for n in range(1, number):
    if number % n == 0:   # evaluates list of divisors
        divisor = n
        sum += divisor    # adds as it identifies divisor
        print(divisor, end = " ")

if sum == number:
    print("\n")
    print(f"{number} is a perfect number.")
else:
    print("\n")
    print(f"{number} is not a perfect number.")
    