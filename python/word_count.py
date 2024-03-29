# This program counts words in a string. Exercise given by ChatGPT.
print("\n\n")

def count_words(string):
    list = string.split()
    return len(list)


def main():

    sentence = input("Type in a sentence to count the words in it: ")

    print (f"\nYour sentence has {count_words(sentence)} words!")


main()