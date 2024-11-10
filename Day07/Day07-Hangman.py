import random
from hangman_words import word_list
import hangman_art


# Define a list of words
lives = 6

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Initialize game variables
game_over = False
correct_letters = []

# Print the game logo
print(hangman_art.logo)

# Create a placeholder with "_" for each letter in the chosen word
placeholder =""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_" 
print("Word to guess: ",placeholder)

# Main game loop
while not game_over:
    print(f"**************************** {lives} / 6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    print(hangman_art.stages[lives])

    
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
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Deduct a life if the guessed letter is incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("***********************YOU LOSE**********************")
            print(f"************CORRECT WORD: {chosen_word} ************")

    # Check if the player has guessed all letters
    
    elif "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    
    print(f"Guess result: {display}")
    
