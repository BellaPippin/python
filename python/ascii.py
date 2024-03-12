# This is an ASCII Value Finder
print ("|n\n")

def main():
    user_input = input("Enter a character:  ")

    while len(user_input) != 1:
        print ("Sorry, it has to be a SINGLE character!")
        user_input = input("Please enter a character:  ")

    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")

main()