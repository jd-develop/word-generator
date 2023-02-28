# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from default_letter_combinations import *
from string import ascii_letters as ascii_l
from pprint import pprint
import random

LETTER_COMBINATIONS = FRENCH_LETTER_COMBINATIONS
CONSONANTS = "bcçdfghjklmnpqrstvwxz"
possible_letters = set()
print("Computing possible letters...")
for trio in LETTER_COMBINATIONS:
    for letter in trio:
        possible_letters.add(letter.lower())


def calculate_probability(trio):
    if LETTER_COMBINATIONS.get(trio) is None:
        return 0
    total = len(LETTER_COMBINATIONS.values())
    if total == 0:
        return 0
    else:
        return (LETTER_COMBINATIONS[trio]*100) / total


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

print("Creating words...")
word = ''
words = []
for word_ in range(words_number):
    # possible_letters is a set
    possible_start_trios_initial = [random.choice(list(LETTER_COMBINATIONS.keys())) for i in range(50)]
    possible_start_trios_cleaned = []
    for e in possible_start_trios_initial:
        if len(e) == 3:
            if not e[0] == e[1]:
                if e[0] not in "-èäâëîïöôüûù":
                    if not (e[0] in CONSONANTS and e[0] in CONSONANTS and e[0] in CONSONANTS):
                        possible_start_trios_cleaned.append(e)
    possible_start_trios_pondered = [e for e in possible_start_trios_cleaned for i in range(LETTER_COMBINATIONS.get(e, 0))]
    word += random.choice(possible_start_trios_pondered)
    while len(word) != letters_in_the_word:
        letter_list = []
        while len(letter_list) == 0:
            for letter in list(possible_letters):
                if len(word) == letters_in_the_word - 1:
                    probability = calculate_probability(word[-1:] + letter) * 100 + calculate_probability(letter) # * 100
                else:
                    probability = calculate_probability(word[-2:] + letter)
                for loop in range(int(probability)):
                    letter_list.append(letter)
            if len(letter_list) == 0:
                word = word[:-1]

        word += random.choice(letter_list)
    new_word = ""
    for i in range(len(word)):
        if i+3 > len(word):
            new_word += word[i]
        elif word[i] == "e" and word[i+1] in CONSONANTS and word[i+2] not in CONSONANTS:
            new_word += "è"
        else:
            new_word += word[i]
    words.append(new_word)
    word = ''

print(words)
