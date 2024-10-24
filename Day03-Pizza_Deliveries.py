print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")

price = 0 # Start from 0 to increase the price later

if size == "S":
    price += 15 # Add the price of small pizza
elif size == "M":
    price += 20 # Add the price of medium pizza
elif size == "L":
    price += 25 # Add the price of large pizza
else:
    print("You typed the wrong inputs")

if pepperoni == "Y": # If add to pepperoni
    if size =="S":
        price += 2 # If the size input have small pizza, increase the price by 2 more 
    else:
        price += 3 # If the size input have medium or large pizza, increase the price by 3 more
if extra_cheese =="Y": 
    price += 1 # If the extra_cheese input have "Y", increase the price by 1 more

print(f"Your final bill is: ${price}.")