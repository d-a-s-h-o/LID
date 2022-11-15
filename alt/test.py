#!/usr/bin/env python3

# This program is used to find the probability that a given word is in a given language, based on the probability that each character in the word is in the language.
import sys
import json

file_suffix = ""


# Import the probabilities file.
def import_probabilities():
    probability_filename = "probabilities.json"
    if file_suffix:
        probability_filename = "probabilities_" + file_suffix + ".json"
    with open(probability_filename, 'r') as probability_file:
        probabilities = json.load(probability_file)
    return probabilities

# Calculate the probability that a given word is in a given language.
def calculate_word_probability(word, language):
    probabilities = import_probabilities()
    word_probability = 1
    for char in word:
        if char in probabilities:
            word_probability *= probabilities[char][language]
        else:
            # If the character is not in the probabilities file, assume it is equally likely to be in any language.
            word_probability *= 0.5
    return word_probability

# Calculate the probability that a given word is in English or French.
def main(word):
    english_probability = calculate_word_probability(word, "english")
    french_probability = calculate_word_probability(word, "french")
    print("English probability: " + str(english_probability))
    print("French probability: " + str(french_probability))
    # Return the language with the higher probability.
    if english_probability > french_probability:
        return english_probability, french_probability, "english"
    elif french_probability > english_probability:
        return english_probability, french_probability, "french"
    else:
        return english_probability, french_probability, "equal"

# Determine whether a given word is more likely to be in English or French, and by how much.
def determine_language(word):
    english_probability, french_probability, language = main(word)
    if language == "english":
        print(f"The word is {round(english_probability / french_probability, 2)} times more likely to be an English word.")
    elif language == "french":
        print(f"The word is {round(french_probability / english_probability, 2)} times more likely to be a French word.")
    else:
        print("The word is equally likely to be in English or French.")

    # Check if the word is in the word lists.
    with open('english_training.txt', 'r') as english_file:
        english_words = english_file.read().splitlines()
    with open('french_training.txt', 'r') as french_file:
        french_words = french_file.read().splitlines()
    english = False
    french = False
    if word in english_words:
        english = True
    if word in french_words:
        french = True
    if english and french:
        print("The word is in both word lists.")
    elif english:
        print("The word is only in the English word list.")
    elif french:
        print("The word is only in the French word list.")

# Run the program with the word given as a command line argument.
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a word to test.")
    else:
        for arg in args:
            if arg == '-h' or arg == '--help':
                print("This program determines whether a given word is more likely to be in English or French, and by how much.")
                print("Usage: test.py [word]")
                sys.exit(1)
            elif arg == "-v" or arg == "--version":
                print("test.py version 1.0")
                sys.exit(1)
            elif arg == "-s" or arg == "--suffix":
                file_suffix = str(args[args.index(arg) + 1])
                determine_language(args[args.index(arg) + 2])
                break
            else:
                determine_language(arg)