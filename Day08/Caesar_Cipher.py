# Alphabet list to map letters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    """ 
    Encrypts the given text using a Caesar Cipher with the specified shift amount.

    Args:
        original_text (str): The text to encrypt.
        shift_amount (int): The number of positions to shift each letter.
    """
    # Initialize an empty string to hold the encrypted text.
    chipper_text = ""

    # Loop through each letter in the original text.
    for letter in original_text:

        # Find the current position of the letter in the alphabet.
        # Shift the position forward by the shift amount.
        shifted_position = alphabet.index(letter) + shift_amount

        # Ensure the position wraps around if it goes past 'z'.
        shifted_position %= len(alphabet)
        
        # Append the encrypted letter to the result string.
        chipper_text += alphabet[shifted_position]
        
    print(chipper_text)

# Call the encrypt function with the user's inputs.
encrypt(text, shift)
        

   


