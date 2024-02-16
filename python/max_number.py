# This program finds the largest number inside nested lists. (Nested list practice)
print ("\n\n")

# Initialize lists
numbers = [[1,30,89,6,94,77],[90, 140, 350],[5, 205, 56]]
max_numbers = []

# Find the biggest number

for number in numbers:
        max_number = max(number)
        max_numbers.append(max_number)

max_number = max(max_numbers)

print (max_number)