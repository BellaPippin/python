# This program checks if a word is a palindrome. Exercise given by ChatGPT.
print("\n\n")

def check_palindrome(string):
    reversed_word = string[::-1]

    if string == reversed_word:
        return True
    else:
        return False


def main():

    word = input("Pick and type a word to check whether it is a palindrome: ")

    if check_palindrome(word):
        print ("\nYay this is a palindrome")
    else:
        print ("\nThis is not a palindrome.")

main()