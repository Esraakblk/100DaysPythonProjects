# Alphabet list to map letters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    """ 
        Encrypts the given text using a Caesar Cipher with the specified shift amount.

        Args:
            original_text (str): The text to encrypt.
            shift_amount (int): The number of positions to shift each letter.
            operation (str): Either 'encode' for encryption or 'decode' for decryption.

        Returns:
            None: Prints the resulting text.

    """
    # Initialize an empty string to hold the encrypted text.
    output_text = ""

    # Loop through each letter in the original text.
    for letter in original_text:

        # Adjust the shift direction for decoding
        if encode_or_decode == "decode":
            shift_amount *= -1
            
        # Find the current position of the letter in the alphabet.
        # Shift the position forward by the shift amount.
        shifted_position = alphabet.index(letter) + shift_amount

        # Ensure the position wraps around if it goes past 'z'.
        shifted_position %= len(alphabet)

        # Append the encrypted letter to the result string.
        output_text += alphabet[shifted_position]
            
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
# Call the encrypt function with the user's inputs.
caesar(text, shift, direction)

        

   


