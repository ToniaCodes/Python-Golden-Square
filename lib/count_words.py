

"""""
Test-drive a function with the following design:

Design

A function called count_words that takes a string

as an argument and returns the number of words in that string.

"""""

from lib.count_words import *

"""""
if given an empty string create a test 
that demonstrate a function retuing an empty string
"""
def test_given_empty_string_return_empty_string():
    result = count_words("")
    assert result == ""

def test_given_a_string_of_words_return_word_length():
    result =count_words("string")
    assert result == 6
