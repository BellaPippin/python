# This program counts vowels in a string. Exercise given by ChatGPT.
print ("\n\n")

def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]

    counter = 0

    string = string.lower()

    for ch in string:
        if ch in vowels:
            counter +=1

    return counter


def main():

    word = input ("Enter something and I'll count the vowels: ")

    print (f"This has {count_vowels(word)} vowels")

main()