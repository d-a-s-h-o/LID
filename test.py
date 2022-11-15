#!/usr/bin/env python3

# This program is used to find the probability that a given word is in a given language, based on the probability that each character in the word is in the language.
import sys # The sys module is used to get the command line arguments.
import json # The json module is used to import the probabilities file.

# Import the probabilities file.
def import_probabilities():
    with open('english_probabilities.json', 'r') as english_probabilities: # Open the file.
        english_probabilities = json.load(english_probabilities) # Load the file.
    with open('french_probabilities.json', 'r') as french_probabilities:
        french_probabilities = json.load(french_probabilities)
    return english_probabilities, french_probabilities # Return the files.


'''
The default probability of a character not being in the language is 1/26. This is because there are 26 letters in the English alphabet, and 26 letters in the French alphabet (that we are considering). If a character is not in the probabilities file, it is assumed to be evenly distributed.

The default probability of a word has to be 1, because the probability of a word is the product of the probabilities of each character in the word. If the probability of a word is 0, then the probability of any character in the word is 0, which is not true. We start with a probability of 1, and work our way down to the true probability.
'''
# Calculate the probability that a given word is in a given language.
def calculate_word_probability(word, language):
    english_probabilities, french_probabilities = import_probabilities()
    word_probability = 1
    if language == "english":
        for character in word:
            if character in english_probabilities:
                word_probability *= english_probabilities[character]
            else:
                word_probability *= 1 / 26 # Evenly distributed.
    elif language == "french":
        for character in word:
            if character in french_probabilities:
                word_probability *= french_probabilities[character]
            else:
                word_probability *= 1 / 26 # Evenly distributed.
    return word_probability

# Calculate the probability that a given word is in English or French.
def main(word):
    english_probability = calculate_word_probability(word, "english")
    french_probability = calculate_word_probability(word, "french")
    # Return the language with the higher probability.
    if english_probability > french_probability:
        return "English"
    elif french_probability > english_probability:
        return "French"
    else:
        return "Equally likely to be in English or French." # This should never happen. If it does, there is most likely a bug in the code. The odds of a word being in both languages is probable, but being equally likely to be in both languages is very very unlikely. That would mean that either each character in the word is equally likely to be in both languages, which is not true for any character, or that the word is comprised of characters that are not in either language, which is a bug, or that the probability of one character is the same as the probability of a different character for the other language, and vice versa, which is incredibly unlikely.

# Run the program with the word given as a command line argument.
if __name__ == "__main__":
    word = sys.argv[1]
    word = word.replace("é", "e").replace("è", "e").replace("ê", "e").replace("ë", "e").replace("à", "a").replace("â", "a").replace("ä", "a").replace("ç", "c").replace("î", "i").replace("ï", "i").replace("ô", "o").replace("ö", "o").replace("ù", "u").replace("û", "u").replace("ü", "u").replace("ÿ", "y").replace("œ", "oe").replace("æ", "ae").replace("ß", "ss").replace(" ", "")
    word = "".join([char for char in word if char.isalpha()]).lower().strip()
    print(main(word))