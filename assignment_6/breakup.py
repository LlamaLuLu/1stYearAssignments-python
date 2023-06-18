# Accepts sentence as input & outputs as comma-separated list of lowercase words with full-stop at end
# Lulama Lingela
# 18 March 2023

user_text = input("Enter a sentence:\n").lower()
list_items = user_text.count(" ")

if list_items == 0:
    new_list = user_text
else:
    new_list = user_text[:user_text.find(" ")]
    for w in range(list_items):   # separates each word in input
        sp1 = user_text.find(" ")
        user_text = user_text[sp1 + 1:]  # removes added word from input
        sp2 = user_text.find(" ")
        if sp2 < 1:
            word = user_text
        else:
            word = user_text[:sp2]
        new_list += ", " + word   # word added to list
print("The word list: " + new_list + ".")