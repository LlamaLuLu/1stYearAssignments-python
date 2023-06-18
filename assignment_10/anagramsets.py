# Search for sets of words that are a specific length & anagrams of each other & writes results to file with given filename.
# Lulama Lingela
# 6 May 2023

def letter_count(word):
    """Counts number of occurrences of each letter in word & returns as dictionary."""
    word = sorted(word.lower())
    counter = {}
    for letter in word:
        if letter in counter:   # adds count for duplicate letter
            counter[letter] += 1
        else:   # counts new letter
            counter[letter] = 1
    return counter


def find_anagrams(og_word, list):
    """Returns list of anagrams of word."""
    anagrams = []
    og_word_count = letter_count(og_word)
    for word in list:
        if (word != og_word) and (og_word_count == letter_count(word)):
            anagrams.append(word)
    if anagrams:
        return anagrams
    else:
        return ""


def main():
    # list of all words in alphabetical order
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
    lexicon.sort()

    print("***** Anagram Set Search *****")
    word_length = int(input("Enter word length:\n"))
    print("Searching...")
    new_filename = input("Enter file name:\n").strip()
    print("Writing results...")

    # list of words of same length
    same_length = []
    for word in lexicon:
        if len(word) == word_length:
            same_length.append(word)

    # search anagram & append to list
    anagram_sets = []   # becomes 2D list of word & anagrams
    for word in same_length:
        word_anagram = find_anagrams(word, same_length)
        pair = [word]
        pair.extend(word_anagram)
        if word_anagram != "":
            if len(anagram_sets) == 0:
                anagram_sets.append(pair)
            # check if word & anagrams not already in final list
            elif sorted(pair) not in anagram_sets:
                anagram_sets.append(pair)
    # for sub_set in anagram_sets:
    #     print(sub_set)

    # saves data in new file
    new_file = open(new_filename, "w")
    for sub_set in anagram_sets:
        if sub_set == anagram_sets[-1]:
            new_file.write(str(sub_set))
        else:
            new_file.write(str(sub_set)+"\n")
    new_file.close()


if __name__ == "__main__":
    main()

