# Write a program that takes a list of numbers as input and then calculates and prints the following:

# The sum of all the numbers in the list.
# The average of all the numbers in the list.
# The largest number in the list.
# The smallest number in the list.
print ("\n\n")

# Initialize list
numbers = []

# Take 5 numbers from user, and append to "numbers".
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Run operations with the numbers on the list.

numbers_sum = sum(numbers) # The sum of all numbers
print (f"\nThe sum of all numbers is {numbers_sum}")

numbers_avg = numbers_sum / len(numbers) # The average of all numbers
print (f"\nThe average of all numbers is {numbers_avg}") 

largest_number = max(numbers) # Show the largest number
print (f"\nThe largest number you entered is {largest_number}")

smallest_number = min(numbers) # Show the smallest number
print (f"\nThe smallest number you entered is {smallest_number}")


# Write a program that takes a list of integers as input and then prints out all the numbers in the list that are divisible by 3 but not divisible by 2. Additionally, calculate and print the sum of these numbers.
print ("\n\n")

# Initialize list
numbers = []

# Take 5 numbers from user, and append to "numbers".
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

new_list = []

# Do magic
for number in numbers:
    if number % 3 == 0 and number % 2 != 0:
        new_list.append (number)

print (new_list)
print (f"\nThe sum of these numbers is {sum(new_list)}.")


