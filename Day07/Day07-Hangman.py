import random

# Define a list of words
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Create a placeholder with "_" for each letter in the chosen word
placeholder =""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_" 
print(placeholder)

# Get a letter guess from the user
guess = input("Guess a letter: ").lower()

# Create a display to show guessed letters in the correct positions
display = ""
for letter in chosen_word:
    if guess == letter:
        display += letter
    else:
        display += "_"
        
print(f"Guess result: {display}")

