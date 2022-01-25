# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from default_letter_combinations import DEFAULT_LETTER_COMBINATIONS
from string import ascii_letters
from pprint import pprint
import random

letter = ascii_letters[:26][random.randint(0, 25)]
word = ''
letters_in_the_word = input("How many letters in the word? ")
try:
    letters_in_the_word = int(letters_in_the_word)
except Exception:
    letters_in_the_word = 5

words_number = input("How many words to create? ")
try:
    words_number = int(words_number)
except Exception:
    words_number = 5

words = []
for word_ in range(words_number):
    for letter_ in range(letters_in_the_word):
        letter = ascii_letters[:26][random.randint(0, 25)]
        word += letter
    words.append(word)
    word = ''


pprint(words)
