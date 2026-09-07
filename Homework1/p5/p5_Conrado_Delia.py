def caesar_cipher(text, shift):

    # Alphabets used for shifting
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encrypted_text = ""

    # Loop through each character in the text
    for char in text:

        # Check for lowercase letters
        if char in lowercase:
            index = lowercase.index(char)
            new_index = (index + shift) % 26
            encrypted_text += lowercase[new_index]

        # Check for uppercase letters
        elif char in uppercase:
            index = uppercase.index(char)
            new_index = (index + shift) % 26
            encrypted_text += uppercase[new_index]

        # Keep spaces, numbers, and punctuation unchanged
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decipher(cyphertext, shift):

    # Alphabets used for shifting
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    deciphered_text = ""

    # Loop through each character
    for char in cyphertext:

        # Check for lowercase letters
        if char in lowercase:
            index = lowercase.index(char)
            new_index = (index - shift) % 26
            deciphered_text += lowercase[new_index]

        # Check for uppercase letters
        elif char in uppercase:
            index = uppercase.index(char)
            new_index = (index - shift) % 26
            deciphered_text += uppercase[new_index]

        # Keep spaces, numbers, and punctuation unchanged
        else:
            deciphered_text += char

    return deciphered_text


def letter_frequency(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Dictionary to store letter counts
    frequency = {}

    # Start each letter at 0
    for letter in alphabet:
        frequency[letter] = 0

    # Loop through the text
    for char in text:

        # Convert character to lowercase
        char = char.lower()

        # Only count alphabetic characters
        if char in alphabet:
            frequency[char] += 1

    return frequency


def main():

    print("Caesar Cipher Program")
    print("---------------------")

    # Get message from user
    message = input("Enter a message: ")

    # Get shift value from user
    shift = int(input("Enter a shift value: "))

    # Encrypt the message
    ciphered_text = caesar_cipher(message, shift)

    # Get letter frequencies
    frequencies = letter_frequency(message)

    # Decrypt the encrypted message
    deciphered_text = caesar_decipher(ciphered_text, shift)

    # Display results
    print("\nCiphered Text:")
    print(ciphered_text)

    print("\nLetter Frequency:")
    for letter in frequencies:
        print(letter, ":", frequencies[letter])

    print("\nDeciphered Text:")
    print(deciphered_text)


# Run the program
if __name__ == "__main__":
    main()