# Searches a file for anagrams of a given word, printing the results in alphabetical order.
# Lulama Lingela
# 2 May 2023

import os.path

def letter_count(word):
    """Counts number of occurrences of each letter in word"""
    word.lower()
    counter = {}
    for letter in word:
        if letter in counter:   # adds count for duplicate letter
            counter[letter] += 1
        else:   # counts new letter
            counter[letter] = 1
    # sorts letters in alphabetical order
    sorted_letters = {}
    for key in sorted(counter):
        sorted_letters[key] = counter[key]
    return sorted_letters

def main():
    print("***** Anagram Finder *****")
    if os.path.isfile("EnglishWords.txt"):  # checks that text file exists
        start = False
        lexicon = []
        word_file = open("EnglishWords.txt", "r")
        for line in word_file:
            if "START" in line:
                start = True
            if start:   # adds words from "START" onwards
                lexicon.append(line.strip())
        word_file.close()
        lexicon.remove("START")
        lexicon.sort()   # list of all words in alphabetical order

        user_word = input("Enter a word:\n").strip()
        anagrams = []
        for word in lexicon:
            if (letter_count(user_word) == letter_count(word)) and (user_word != word):
                anagrams.append(word)
        if anagrams:
            print(anagrams)
        else:
            print(f"Sorry, anagrams of '{user_word}' could not be found.")
    else:
        print("Sorry, could not find file 'EnglishWords.txt'.")

if __name__ == "__main__":
    main()
