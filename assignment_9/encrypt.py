# Uses a recursive function to encrypt a message by converting all lowercase characters to next character
# Lulama Lingela
# 26 April 2023

def encrypt(str):
    if len(str) == 0:   # base case
        return ""
    # recursive call
    elif str[0] == "z":   # from z to a
        return "a" + encrypt(str[1:])
    elif str[0].isalpha():   # changes to next character if in alphabet & lowercase
        if str[0] != str[0].upper():
            return chr(ord(str[0]) + 1) + encrypt(str[1:])
        else:
            return str[0] + encrypt(str[1:])
    else:
        return str[0] + encrypt(str[1:])


def main():
    user_txt = input("Enter a message:\n")
    print(f"Encrypted message:\n{encrypt(user_txt)}")

if __name__ == "__main__":
    main()
