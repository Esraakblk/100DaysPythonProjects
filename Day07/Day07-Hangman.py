import random

# Define a list of words
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Initialize game variables
game_over = False
correct_letters = []

# Create a placeholder with "_" for each letter in the chosen word
placeholder =""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_" 
print(placeholder)

# Main game loop
while not game_over:
    guess = input("Guess a letter: ").lower()
    
    # Create a display to show guessed letters in the correct positions
    display = ""
    
    # Update display based on the guessed letter    
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Guess result: {display}")
    # Check if the player has guessed all letters
    if "_" not in display:
        game_over = True
        print("You win")


# Create a display to show guessed letters in the correct positions



