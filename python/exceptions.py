# Simple Python program to calculate the square of a number

# Define the function.
def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

    except ValueError:
        print("You have to enter a number!")
        square_number()
    
# Call function
square_number()