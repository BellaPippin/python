# Write a Python function named count_vowels that takes a string as input and returns the count of vowels in the string.

def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for letter in string:
        if letter in vowels:
            counter += 1
    return counter


          
string = input("Enter a word to count its vowels:  ")

print ("This word has", count_vowels(string), "vowels.")