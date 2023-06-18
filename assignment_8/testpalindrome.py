# Devising set of 8 test cases for function that cumulatively achieves path coverage (doctest script)
# Lulama Lingela
# 13 April 2023

# test for is_palindrome() module: accepts string as parameter & determines whether it is a palindrome or not
# critical lines: line 9 to 16

"""
>>> import palindrome
>>> palindrome.is_palindrome("")   # not s
True
>>> palindrome.is_palindrome("a")   # s, len(s) == 1
True
>>> palindrome.is_palindrome("and")   # s, len(s) > 1, s[i] != s[-i-1]
False
>>> palindrome.is_palindrome("racecar")   # s, len(s) > 1, s[i] == s[-i-1]
True
>>> palindrome.is_palindrome("a santa at nasa")   # s, len(s) > 1, s[i] != s[-i-1], but letters palindromic
False

"""
import doctest
doctest.testmod(verbose=True)