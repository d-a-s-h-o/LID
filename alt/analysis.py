#!/usr/bin/env python3

# This program is used to visualize the character frequency data from train.py.

# Import the character frequency data.
import json # Used to import the character frequency data.
import matplotlib.pyplot as plt # Used to plot the data.
import numpy as np # Used to create the x-axis.
from matplotlib.font_manager import FontProperties

font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_size(16)
font.set_style('normal')

# Import the character frequency data.
with open("probabilities.json", "r") as probabilities: # Open the file.
    probabilities = json.load(probabilities) # Load the data.

# Create a list of the characters a-z.
characters = 'abcdefghijklmnopqrstuvwxyz' # Create a list of the characters a-z.

# Create a list of the probabilities of each character in English.
english = {} # Create a dictionary to store the probabilities.
for character in characters: # Loop through each character.
    english[character] = probabilities[character]['english'] # Add the probability to the dictionary.

# Create a list of the probabilities of each character in French.
french = {} # Create a dictionary to store the probabilities.
for character in characters: # Loop through each character.
    french[character] = probabilities[character]['french'] # Add the probability to the dictionary.

# Create a list of the probabilities of each character in English and French.
english = list(english.values()) # Create a list of the probabilities.
french = list(french.values()) # Create a list of the probabilities.

# Turn characters into a list
characters = list(characters) # Turn characters into a list.

# Create a scatter plot of the probabilities of each character in English and French.
fig, ax = plt.subplots() # Create a figure and axes.
ax.stem(characters, english, label="English", use_line_collection=True, markerfmt="bo") # Plot the English data.
ax.stem(characters, french, label="French", use_line_collection=True, markerfmt="ro") # Plot the French data.
ax.set_xlabel("Character", fontproperties=font) # Set the x-axis label.
ax.set_ylabel("Probability", fontproperties=font) # Set the y-axis label.
ax.set_title("Character Frequency", fontproperties=font) # Set the title.
ax.legend(prop=font) # Add a legend.
plt.show() # Show the plot.