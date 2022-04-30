# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from default_letter_combinations import *
from string import ascii_letters as ascii_l
from pprint import pprint
import random

ascii_letters = ascii_l[:26]


def calculates_probability(couple):
    total = 0
    try:
        if FRENCH_LETTER_COMBINATIONS[couple] is None:
            return 0
    except KeyError:
        return 0
    for couple_ in FRENCH_LETTER_COMBINATIONS:
        if FRENCH_LETTER_COMBINATIONS[couple_] is not None:
            total += FRENCH_LETTER_COMBINATIONS[couple_]
    if total == 0:
        return 0
    else:
        return (FRENCH_LETTER_COMBINATIONS[couple]*100) / total


letter = ascii_letters[random.randint(0, 25)]
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
    letter = ascii_letters[random.randint(0, 25)]
    word += letter
    for letter_ in range(letters_in_the_word):
        letters = []
        for loop in range(10):
            letters.append(ascii_letters[random.randint(0, 25)])
        letter_list = []
        for letter in letters:
            if letter_ == letters_in_the_word - 1:
                probability = calculates_probability(word[:1] + letter) * calculates_probability(letter) * 50
            else:
                probability = calculates_probability(word[:1] + letter)
            for loop in range(int(probability * 500)):
                letter_list.append(letter)
        best_letter = random.choice(letter_list)
        word += best_letter
    words.append(word)
    word = ''

pprint(words)
