

# Project: Password Generator
"""
Description: This project creates a simple password generator that generates strong and random passwords based on user-defined criteria.
Users can specify the length of the password and choose whether it should include uppercase letters, lowercase letters, numbers, and special characters.
"""
# Steps:

# Ask the user for the desired length of the password.
# Prompt the user to specify if the password should include uppercase letters, lowercase letters, numbers, and special characters.
# Generate a random password based on the user's criteria.
# Display the generated password to the user.
# Requirements:

import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        return "Error: No valid characters selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    desired_length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(
        desired_length,
        uppercase=include_uppercase,
        lowercase=include_lowercase,
        numbers=include_numbers,
        special_chars=include_special_chars
    )

    print("Generated Password:", password)


