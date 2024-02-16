# Exercise: Accessing Items Inside Nested Lists with Error Handling

# Write a Python program that allows the user to input row and column indices and then prints the corresponding item in a nested list. Your program should handle errors gracefully, such as invalid indices or non-integer inputs.

# For example, given the nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]], your program should prompt the user to enter row and column indices. If the user enters 2 for the row and 3 for the column, the program should print the item at row 2, column 3 (which is 6). If the user enters invalid indices or non-integer inputs, the program should display an appropriate error message.

# This exercise will help you practice accessing specific items within nested lists and handling potential errors that may occur during user input.

print ("\n\n")

# Initialize list
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Get user input for indices
index_a = int(input("Enter a number 0-2 for the first index: "))
index_b = int(input("Enter a number 0-2 for the second index: "))

if isinstance (index_a, int):
    if isinstance (index_b, int):
        if index_a >= 0 and index_a < 3:
            if index_b >= 0 and index_b < 3:
                print (my_list[index_a][index_b])
            else:
                print ("Oops something went wrong. Try again.")
        else:
            print ("Oops something went wrong. Try again.")
    else:
        print ("Oops something went wrong. Try again.")
else:
    print ("Oops something went wrong. Try again.")

