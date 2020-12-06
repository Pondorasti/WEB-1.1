import pytest
import unittest

from .string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected

def test_reverse_long():
    """Test reversing a long string."""
    expected = reverse("Hey Alex")
    actual = 'xelA yeH'
    assert actual == expected

def test_reverse_short():
    """Test reversing a short string."""
    expected = reverse("Alex")
    actual = "xelA"
    assert actual == expected

def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = reverse_words("Hey Alex")
    actual = "yeH xelA"
    assert actual == expected

def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = reverse_words("Alex")
    actual = "xelA"
    assert actual == expected

def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = sarcastic("Hey Alex")
    actual = "HeY aLeX"
    assert actual == expected

def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = sarcastic("Alex")
    actual = "AlEx"
    assert actual == expected

# run the tests
if __name__ == '__main__':
    unittest.main()