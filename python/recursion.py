# This program calculates factorials
print ("\n\n")

# this function calculates the factorial
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# 'main' runs the program
def main():
    print ("Hello! Let's calculate some factorials!")
    number = int(input("Please enter a non-negative integer:  "))
    print (f"The factorial of {number} is {factorial(number):,.2f}\n\n")




main()