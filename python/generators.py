# This program takes a list of different characters and shows all possible combinations.
print ("\n\n")

# Take each character and pair it with each character on the list
def two_letter_combinations(chars):
    for char1 in chars:
        for char2 in chars:
            yield char1 + char2

def main():

    list_of_chars = ['d', 'u', 'c', 'k', 's']
    combinations = two_letter_combinations(list_of_chars)

    print (f"Combinations possible from {list_of_chars}:")

    for combination in combinations:
        print (combination)

main()