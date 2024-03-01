# Creating and using dictionaries
# This program translates words into the NATO alphabet.
print ("\n\n")

# Initialize dictionary
nato_dictionary = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliette",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-Ray",
    "Y": "Yankee",
    "Z": "Zulu" }

# This function takes the user input, converts it to uppercase and converts it into the NATO alphabet.
def spell_word():
    user_word = input("Write a word: ")
    upper_word = user_word.upper()

    for letter in upper_word:
        if letter in nato_dictionary:
            print(nato_dictionary[letter])


def main():
    spell_word()


main()