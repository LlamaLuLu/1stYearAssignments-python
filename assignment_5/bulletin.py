# Simulates simple BBS with 1 stored message & 2 fixed files
# Lulama Lingela
# 13 March 2023

end = False
message = ""
file1 = "42.txt"
file2 = "1015.txt"

while end is False:
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    user_choice = input("Enter your selection:\n")
    # option1: enter message
    if user_choice == "E" or user_choice == "e":
        message = input("Enter the message:\n")
    # option2: view message
    elif user_choice == "V" or user_choice == "v":
        if message == "":
            print("The message is: no message yet")
        else:
            print(f"The message is: {message}")
    # option3: list files
    elif user_choice == "L" or user_choice == "l":
        print(f"List of files: {file1}, {file2}")
    # option4: display file
    elif user_choice == "D" or user_choice == "d":
        file_search = input("Enter the filename:\n")
        if file_search == file1:
            print("The meaning of life is blah blah blah ...")
        elif file_search == file2:
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    # option5: exit program
    elif user_choice == "X" or user_choice == "x":
        print("Goodbye!")
        end = True
    # option6: no choice made
    else:
        print("Please select an option.")
        end = False
