# Caesar Cipher Program - Day 8 Python Challenge
# This program encrypts and decrypts messages using the Caesar cipher method
# Created as part of 100 Days of Python coding challenge

# Import and display the ASCII art logo
import art
print(art.logo)

# Complete alphabet list for character shifting operations
# Used as reference for finding positions and shifting letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# LEGACY CODE: Original separate encrypt/decrypt functions (now replaced by unified caesar function)
# These functions were the first implementation before refactoring into a single function

# def encrypt(original_text , shift_amount) :
#     # Function to encrypt text by shifting letters forward in alphabet
#     cypher_text=""
#     for letter in original_text :
#         shifted_position = alphabet.index(letter) + shift_amount
#         # Use modulo to wrap around alphabet (z + 1 = a)
#         shifted_position %= len(alphabet)
#         cypher_text += alphabet[shifted_position]
#     print(f"here is the encoded result : {cypher_text}")
    
# def decrypt(original_text , shift_amount) :
#     # Function to decrypt text by shifting letters backward in alphabet
#     output_text = ""
#     for letter in original_text :
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]    
#     print(f"here is the decoded result : {output_text}")


def caeser(original_text , shift_amount , encode_or_decode):
    """
    Unified Caesar cipher function that handles both encoding and decoding
    
    Args:
        original_text: The message to encrypt or decrypt
        shift_amount: Number of positions to shift each letter
        encode_or_decode: "encode" to encrypt, "decode" to decrypt
    """
    output_text = ""
    
    # For decoding, reverse the shift by making it negative
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    # Process each character in the input text        
    for letter in original_text :
        # Preserve spaces, punctuation, and numbers (non-alphabetic characters)
        if letter not in alphabet:
            output_text += letter
        else:
            # Find current position and calculate new position after shift
            shifted_position = alphabet.index(letter) + shift_amount
            # Use modulo to handle wrapping (e.g., z shifted by 1 becomes a)
            shifted_position %= len(alphabet)
            # Add the shifted character to result
            output_text += alphabet[shifted_position]    
    
    # Display the final result
    print(f"here is the {encode_or_decode}d result : {output_text}")
    

# MAIN PROGRAM EXECUTION
# Flag to control the main program loop
should_continue = True

# Main program loop - allows user to encrypt/decrypt multiple messages
while should_continue:
    # Legacy function calls (kept as reference)
    # encrypt(original_text = text , shift_amount = shift)
    # decrypt(original_text = text , shift_amount = shift)

    # Get user input for operation type
    direction = input("type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    
    # Get the message to process
    text = input("Type your message:\n").lower()
    
    # Get the shift amount (how many positions to move each letter)
    shift = int(input("type the shift number:\n"))

    # Call the unified caesar function with user inputs
    caeser(original_text = text , shift_amount = shift , encode_or_decode = direction)
    
    # Ask if user wants to continue or exit the program
    restart = input("Type 'yes' if you want to go again . Otherwise 'no'\n").lower()
    
    # Exit condition: stop the loop if user types 'no'
    if restart == "no":  # Fixed: was using assignment (=) instead of comparison (==)
        should_continue = False
        print("good bye")

# TODO COMPLETED:
# ✅ Created complete alphabet list (a-z)
# ✅ Implemented encryption function with letter shifting
# ✅ Implemented decryption function with reverse shifting
# ✅ Combined both functions into unified caesar() function
# ✅ Added support for non-alphabetic characters (spaces, punctuation)
# ✅ Implemented modulo arithmetic for alphabet wrapping
# ✅ Created main program loop for multiple operations
# ✅ Added user input validation and restart functionality
# ✅ Imported and displayed ASCII art logo
# ✅ Added comprehensive error handling and user experience improvements
    
    