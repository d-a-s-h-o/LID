#!/usr/bin/env python3

# This program is used to find the probability that a given character appears in a random word for a given language.

# Import the two word lists (.txt files) that we will be using.
import sys
import json

# Set verbose to false as default.
verbose = False

# Import the two word lists (.txt files) that we will be using.
def import_word_lists():
    english_words = []
    french_words = []
    with open('english_training.txt', 'r') as english_file:
        english_words = english_file.read().splitlines()
    with open('french_training.txt', 'r') as french_file:
        french_words = french_file.read().splitlines()
    return english_words, french_words

# Count the total number of characters in a given word list.
def count_characters_in_word_list(word_list):
    count = 0
    for word in word_list:
        for char in word:
            count += 1
    return count

# Count how often a given character appears in a given word list.
def count_character_in_word_list(character, word_list):
    count = 0
    for word in word_list:
        for char in word:
            if char == character:
                count += 1
    return count

# Calculate the probability that a given character appears in a random word for a given language.
def main(character):
    global verbose
    english_words, french_words = import_word_lists()
    character = character.lower()
    english_count = count_character_in_word_list(character, english_words)
    french_count = count_character_in_word_list(character, french_words)
    english_total = count_characters_in_word_list(english_words)
    french_total = count_characters_in_word_list(french_words)
    english_probability = english_count / english_total
    french_probability = french_count / french_total
    if verbose:
        # Print english count is pretty number
        print(f"English count: {english_count:,}")
        print(f"French count: {french_count:,}")
        print(f"English total: {english_total:,}")
        print(f"French total: {french_total:,}")
    print("English probability: " + str(english_probability))
    print("French probability: " + str(french_probability))
    if verbose:
        print(f"E to F ratio: {english_probability / french_probability}")

# Print json of the probabilities for each character (a-z) to file.
def print_probabilities():
    probabilities = {}
    for character in "abcdefghijklmnopqrstuvwxyz":
        english_words, french_words = import_word_lists()
        english_count = count_character_in_word_list(character, english_words)
        french_count = count_character_in_word_list(character, french_words)
        english_total = count_characters_in_word_list(english_words)
        french_total = count_characters_in_word_list(french_words)
        english_probability = english_count / english_total
        french_probability = french_count / french_total
        probabilities[character] = {
            "english": english_probability, "french": french_probability}
    with open('probabilities.json', 'w') as probabilities_file:
        probabilities_file.write(json.dumps(probabilities))

# Run the program.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            if sys.argv[2] == "-v":
                verbose = True
            else:
                verbose = False
        main(sys.argv[1])
    else:
        print_probabilities()


