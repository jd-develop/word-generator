# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from default_letter_combinations import *
from string import ascii_letters as ascii_l
from pprint import pprint
import random

LETTER_COMBINATIONS = FRENCH_LETTER_COMBINATIONS
possible_letters = set()
for couple in LETTER_COMBINATIONS:
    for letter in couple:
        possible_letters.add(letter.lower())
print(possible_letters)


def calculate_probability(couple):
    total = 0
    if LETTER_COMBINATIONS.get(couple) is None:
        return 0
    for couple_ in LETTER_COMBINATIONS:
        if LETTER_COMBINATIONS[couple_] is not None:
            total += LETTER_COMBINATIONS[couple_]
    if total == 0:
        return 0
    else:
        return (LETTER_COMBINATIONS[couple]*100) / total


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

word = ''
words = []
for word_ in range(words_number):
    # possible_letters is a set
    while (letter := random.choice(list(possible_letters))) in "-ôêàïöûëùèäü":  # totally arbitrary
        letter = random.choice(list(possible_letters))
    word += letter
    for letter_ in range(letters_in_the_word):
        letter_list = []
        for letter in list(possible_letters):
            if letter_ == letters_in_the_word - 1:
                probability = calculate_probability(word[:1] + letter) + calculate_probability(letter) * 50
            else:
                probability = calculate_probability(word[:1] + letter)
            for loop in range(int(probability * 500)):
                letter_list.append(letter)
        try:
            best_letter = random.choice(letter_list)
        except IndexError:
            print(word)
            print(letter_list)
            raise
        word += best_letter
    words.append(word)
    word = ''

pprint(words)
