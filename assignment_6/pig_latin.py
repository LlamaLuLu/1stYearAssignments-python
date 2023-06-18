# To convert from English to a variant of Pig Latin
# Lulama Lingela
# 18 March 2023

vowels = ["a", "e", "i", "u", "o"]

def translator(word):   # translates word into pig-latin
    if word[0] in vowels:
        new_word = word + "way"
        return new_word
    else:
        for v in word:
            if v in vowels:
                vowel_i = word.find(v)
                break
        con = word[:vowel_i]
        new_word = word[vowel_i:] + "a" + con + "ay"
        return new_word

user_text = input("Enter a sentence:\n").lower()
list_items = user_text.count(" ") + 1
new_list = ""

for w in range(list_items):   # separates each word in input
    sp1 = user_text.find(" ")
    if w == list_items - 1:
        word = user_text
    else:
        word = user_text[:sp1]
    new_list += translator(word) + " "   # translates word & adds to new sentence
    user_text = user_text[sp1 + 1:]   # removes translated word from input
print(new_list)