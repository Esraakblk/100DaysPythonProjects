import random
import string

# Lists of possible characters for the password generation
letters = string.ascii_letters # Includes both lowercase and uppercase letters
numbers = string.digits        # Includes digits from 0 to 9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] # List of symbols

print("Welcome to the Pypassword_list Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initializing an empty list for password components
password_list = []

# Adding random letters to the password_list
password_list += random.choices(numbers, k=nr_numbers)

# Adding random symbols to the password_list
password_list += random.choices(symbols, k=nr_symbols)

# Display the password list before shuffling (order not finalized yet)
print("Password list before shuffle:", password_list)

# Shuffle the list to randomize the order of characters
random.shuffle(password_list)
print("Password list after shuffle:",password_list)

# Joining the list into a single string for the final password
password = "".join(password_list)


print(f"Your password is: {password}")
