# This program is a 'guess the number' game.
print ("\n\n")

# import random module and generate a random number 1-100
import random

random_number = random.randrange (1, 100)

# Print function for testing purposes
# print (random_number)

def main():
    number = True

    while number:
        number = int(input("Guess the number 1-100:  "))
        if number == random_number:
            break
        else:
            number_diff = random_number - number
            if abs(number_diff) < 5:
                print ("Very Hot!")
            elif abs(number_diff) < 15:
                print ("Hot!")
            elif abs(number_diff) < 25:
                print ("Cool...try again")
            else:
                print ("Cold! Try again")


main()
print ("You guessed the number!")