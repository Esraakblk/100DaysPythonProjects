import random

# ASCII art for rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ASCII art for scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def rock_paper_scissors():
    # Welcome message for the game
    print("Welcome to the Rock Paper Scissors Game!")
    
    # Get the user's choice and convert it to lowercase
    input_choice = input("What do you choose? Rock, Paper, Scissors:\n").lower()

    # Map the user's choice to the corresponding ASCII art
    if input_choice == "rock":
        user_choice = rock
    elif input_choice == "paper":
        user_choice = paper
    elif input_choice == "scissors":
        user_choice = scissors
    else:
        # If the user input is invalid, return early
        print("You entered the wrong word. Try again!")
        return 

    # Randomly select the computer's choice
    computer_choice = random.choice((rock, paper, scissors))

    # Display the choices and determine the outcome
    print(f"Your choice:\n {user_choice}")
    print(f"Computer choice:\n {computer_choice}")

    # Check for a draw
    if computer_choice == user_choice:
        print("It's a draw")
    # Determine the winner
    elif (user_choice == rock and computer_choice == paper) or \
         (user_choice == paper and computer_choice == scissors) or \
         (user_choice == scissors and computer_choice == rock):
        print("Computer wins!")
    else:
        print("You win!")

# Call the function to play the game
rock_paper_scissors()
