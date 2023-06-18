# Calculates number of k-permutations of n items.
# Lulama Lingela
# 3 April 2023

def get_integer(s):
    """Accepts integer 's' from user."""
    num = input(f"Enter {s}:\n")
    while not num.isdigit():
        num = input(f"Enter {s}:\n")
    num = eval(num)
    return num
    

def calc_factorial(n):
    """Iteratively calculates factorial of integer 'n'."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    n = get_integer(input("Enter n:\n"))
    k = get_integer(input("Enter k:\n"))
    n_factorial = calc_factorial(n)
    nk_factorial = calc_factorial(n - k)
    print("Number of permutations:", n_factorial // nk_factorial)


if __name__ == "__main__":
    main()
