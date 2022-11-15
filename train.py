#!/usr/bin/env python3

# This program is used to find the probability that a given character appears in a random word for a given language.

# Import the two word lists (.txt files) that we will be using.
import sys
import json

# Set verbose to false as default.
language = None # Set the language to None.

# Import the word lists as stdin.
def import_word_lists():
    global language
    english_words = [] # Create an empty list for the English words.
    french_words = [] # Create an empty list for the French words.
    for line in sys.stdin: # For each line in the input...
        line = line.strip() # Remove the newline character.
        line = line.replace("é", "e").replace("è", "e").replace("ê", "e").replace("ë", "e").replace("à", "a").replace("â", "a").replace("ä", "a").replace("ç", "c").replace("î", "i").replace("ï", "i").replace("ô", "o").replace("ö", "o").replace("ù", "u").replace("û", "u").replace("ü", "u").replace("ÿ", "y").replace("œ", "oe").replace("æ", "ae").replace("ß", "ss") # Replace accented characters with their unaccented counterparts.
        line = "".join([char for char in line if char.isalpha()]) # Remove all non-alphabetic characters
        if line == "ENGLISH": # If the line is "ENGLISH"...
            language = "english" # Set the language to English.
        elif line == "FRENCH": # If the line is "FRENCH"...
            language = "french" # Set the language to French.
        else: # If the line is not "ENGLISH" or "FRENCH"...
            line = line.lower() # Set the line to lowercase.
            if language == "english": # If the language is English...
                english_words.append(line) # Add the line to the English word list.
            elif language == "french": # If the language is French...
                french_words.append(line) # Add the line to the French word list.
            else: # If the language is not set...
                # This should never happen.
                print("Error: Language not set.") # Print an error message.
                sys.exit(1) # Exit the program.
    if language == "english": # If the language is English...
        return english_words # Return the English word list.
    elif language == "french": # If the language is French...
        return french_words # Return the French word list.
    else: # If the language is not set...
        # This should never happen.
        print("Error: Language not set.") # Print an error message.
        sys.exit(1) # Exit the program.


def count_characters_in_word_list(word_list): # Count the total number of characters in a word list.
    count = 0 # Set the count to 0.
    for word in word_list: # For each word in the word list...
        for char in word: # For each character in the word...
            count += 1 # Add one to the count.
    return count # Return the count.

def count_character_in_word_list(character, word_list): # Count the number of times a character appears in a word list.
    count = 0 # Set the count to 0.
    for word in word_list: # For each word in the word list...
        for char in word: # For each character in the word...
            if char == character: # If the character is the character we are looking for...
                count += 1 # Add one to the count.
    return count # Return the count.

def print_probabilities(): # Print the probabilities for each character.
    probabilities = {} # Create an empty dictionary for the probabilities.
    words = import_word_lists() # Import the word lists.
    for character in "abcdefghijklmnopqrstuvwxyz": # For each character in the alphabet...
        probabilities[character] = main(character, words) # Add the probability of the character to the dictionary.
    if language == "english": # If the language is English...
        with open('english_probabilities.json', 'w') as outfile: # Open the English probabilities file...
            json.dump(probabilities, outfile) # Write the probabilities to the file.
    elif language == "french": # If the language is French...
        with open('french_probabilities.json', 'w') as outfile: # Open the French probabilities file...
            json.dump(probabilities, outfile) # Write the probabilities to the file.
    else: # If the language is not set...
        # This should never happen.
        print("Error: Language not set.") # Print an error message.
        sys.exit(1) # Exit the program.

def main(character, words=None): # Find the probability that a character appears in a random word.
    global verbose # Import the verbose variable.
    global language # Import the language variable.
    word_list = words # Set the word list to the word list passed to the function.
    character = character.lower() # Set the character to lowercase.
    count = count_character_in_word_list(character, word_list) # Count the number of times the character appears in the word list.
    total = count_characters_in_word_list(word_list) # Count the total number of characters in the word list.
    probability = count / total # Calculate the probability.
    return probability # Return the probability.

if __name__ == "__main__":
    print_probabilities() # Print the probabilities for each character.