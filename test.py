#!/usr/bin/env python3

# This program is used to find the probability that a given word is in a given language, based on the probability that each character in the word is in the language.
import sys
import json

# Import the probabilities file.
def import_probabilities():
    with open('probabilities.json', 'r') as probabilities_file:
        probabilities = json.load(probabilities_file)
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

# Run the program with the word given as a command line argument.
if __name__ == "__main__":
    word = sys.argv[1]
    determine_language(word)