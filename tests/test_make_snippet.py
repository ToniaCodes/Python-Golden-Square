""" 

A function called make_snippet that takes a string
as an argument and returns the first five words and t
hen a '...' 
if there are more than that. 

"""
from lib.make_snippet import *

"""

If given an empty string 
it returns an empty string 

"""
def test_given_empty_string_returns_empty_string():
    result = make_snippet('')
    assert result == ""
"""

if given a string with an argument
it returns the argument in the form of a string 

"""

"""""
Given a string of four words
it returns the same string

"""
def test_given_four_word_string_return_same_string():
    result = make_snippet("one two three four")
    assert result == "one two three four"


""""

if given five words
it reutrns the same string

"""
def test_given_five_word_string_return_same_string():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"



""""
if given a string of six words 
it returns the first five words and ellipsis '...'

"""
def test_given_six_word_string_return_same_string():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."