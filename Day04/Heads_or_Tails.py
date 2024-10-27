import random

def heads_or_tails():
    print("Welcome to the Heads or Tails game!")
    
    # Make a random choice between Heads or Tails
    outcome = random.choice(["Heads", "Tails"])

    # Get the user's guess
    user_guess = input("What is your guess? Type 'Heads' or 'Tails': ").capitalize()

    # Check the guess and display the result
    if user_guess == outcome:
        print(f"You guessed {user_guess} and it's {outcome}. You win!")
    else:
        print(f"You guessed {user_guess} and it's {outcome}. You lose!")

#Run the game
heads_or_tails()






