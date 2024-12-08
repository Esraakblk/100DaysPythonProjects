from art import logo
print(logo)

# Initialize the bids dictionary
bids = {}
continue_bidding = True
while continue_bidding:

    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid?: $"))
    bids[user_name] = user_bid

    other_pricers = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
     # Check if there are other bidders
    if other_pricers == "no":  
        continue_bidding = False
        # Find the highest bidder
        winner = max(bids, key = bids.get)
        print(f"The winner is {winner} with a bid of ${bids[winner]}")
    elif other_pricers == "yes":
        # Clear the console for the next bidder
        print("\n"*50)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")


