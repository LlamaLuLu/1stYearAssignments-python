# Uses a recursive function to find all palindromic primes between two integers N & M supplied as input
# Lulama Lingela
# 26 April 2023

from math import sqrt, floor
import sys
sys.setrecursionlimit(30000)


def check_prime(num, div=3):
    """Returns True if number is prime."""
    if (num == 0) or (num == 1):
        return False
    if (num % 2 == 0) and (num != 2):
        return False
    if (num % div == 0) and (num != div):
        return False
    if (floor(sqrt(num)) <= div):  # optimisation: minimise recursion
        return True
    return check_prime(num, div + 2)


def check_palindrome(num):
    """Returns True if string is palindromic."""
    if len(num) == 0:  # base case: empty string
        return True
    else:
        if num[0] == num[-1]:  # recursive call: checks if each beginning and end character pair equal
            return check_palindrome(num[1:-1])
        else:
            return False


def palindrome_prime(n, m):
    if n > m:  # base case: stops when number = m
        return ""
    elif check_prime(n) and check_palindrome(str(n)):  # recursive call: checks if prime & palindromic
        return f"{n}\n{palindrome_prime(n + 1, m)}"
    else:
        return palindrome_prime(n + 1, m)


def main():
    start = int(input("Enter the starting point N:\n"))
    end = int(input("Enter the ending point M:\n"))
    print(f"The palindromic primes are:\n{palindrome_prime(start, end)}", end="")


if __name__ == "__main__":
    main()
