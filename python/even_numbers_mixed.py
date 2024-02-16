# This program counts the amount of even numbers inside nested lists with different types
print ("\n\n")

# Initialize list
my_list = [["Apple", 3, 6, "String"],["IDK", 10, True, "Meh"],[20, 43, 42, "Yahoo"]]
counter = 0

# Find even numbers and add it to counter
for item in my_list:
    for i in item:
        if isinstance(i, int):  # Check if the item is an integer
            if i % 2 == 0:  # Check if the integer is even
                counter += 1

print (counter)
