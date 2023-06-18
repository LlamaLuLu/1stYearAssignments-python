# Devising set of 8 test cases for function that cumulatively achieves path coverage (doctest script)
# Lulama Lingela
# 13 April 2023

# test for asword() module: accepts int (0-999) as parameter & returns English equivalent
# critical lines: line 15 to 30
"""
>>> import numberutil
>>> numberutil.aswords(100)   # h > 0, rem == 0
'one hundred'
>>> numberutil.aswords(101)   # h > 0, rem > 0, rem < 21
'one hundred and one'
>>> numberutil.aswords(121)   # h > 0, rem > 0, rem >= 21, u > 0
'one hundred and twenty one'
>>> numberutil.aswords(230)   # h > 0, rem > 0, rem >= 21, u == 0
'two hundred and thirty'
>>> numberutil.aswords(20)   # h == 0, rem > 0, rem < 21
'twenty'
>>> numberutil.aswords(99)   # h == 0, rem > 0, rem >= 21, u > 0
'ninety nine'
>>> numberutil.aswords(80)   # h == 0, rem > 0, rem >= 21, u == 0
'eighty'
>>> numberutil.aswords(0)   # h == 0, rem == 0
'zero'

"""
import doctest
doctest.testmod(verbose=True)
