# This program finds the largest numbers inside a nested list. (Nested list practice)
print ("\n\n")

# Initialize lists
numbers = [[1,30,89,6,94,77],[90, 140, 350],[5, 205, 56]]
max_numbers = []

# Find the biggest number

for number in numbers:
        max_number = max(number)
        max_numbers.append(max_number)

print (max_numbers)