# This program counts the amount of even numbers within nested lists. (Nested list practice)
print ("\n\n")

# Initialize lists
numbers = [[1,30,89,6,94,77],[90, 140, 350],[5, 205, 56]]
counter = 0

# Find even numbers and add "1" to a counter each time it finds one
for number in numbers:
    for item in number:
        if item % 2 == 0:
            counter += 1

print (counter)