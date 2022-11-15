#!/usr/bin/env python3

# This program is used to generate strings on the fly, based on the probability that each character in the string is in the language.

import sys  # The sys module is used to get the command line arguments.
import json  # The json module is used to import the probabilities file.
import random  # The random module is used to generate random numbers.

# Language selection. Also makes sure the user entered a valid language.
language = sys.argv[1].lower()
if language == "english":
    pass
elif language == "french":
    pass
else:
    print("Invalid language. Check your spelling and try again.")
    sys.exit(1)
length = int(sys.argv[2])  # Length of the string to be generated.

# Import the probabilities file.
def import_probabilities(language):
    if language == "english":
        with open('english_probabilities.json', 'r') as english_probabilities: # Open the file.
            english_probabilities = json.load(english_probabilities) # Load the file.
        return english_probabilities # Return the file.
    # Same as above, but for French.
    elif language == "french":
        with open('french_probabilities.json', 'r') as french_probabilities:
            french_probabilities = json.load(french_probabilities)
        return french_probabilities

# Generate a string.
def generate_string(language, length):
    probabilities = import_probabilities(language)
    string = ""
    for i in range(length):
        string += random.choices(list(probabilities.keys()),
                                 weights=list(probabilities.values()), k=1)[0] # This line is a bit complicated. It generates a random character based on the probabilities of each character in the language.
    return string


# Run the program.
if __name__ == "__main__":
    print(generate_string(language, length))
