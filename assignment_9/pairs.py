# Uses a recursive function to count the no. of pairs of consecutive characters in string
# Lulama Lingela
# 26 April 2023

def count_doubles(str):
    if len(str) == 1 or len(str) == 0:   # base case
        return 0
    # recursive call
    elif str[0] == str[1]:   # same consecutive letters; exclude pair
        return 1 + count_doubles(str[2:])
    else:   # different letters; next character
        return count_doubles(str[1:])

def main():
    user_txt = input("Enter a message:\n")
    print(f"Number of pairs: {count_doubles(user_txt)}")

if __name__ == "__main__":
    main()