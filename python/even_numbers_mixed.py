# This program counts the amount of even numbers inside nested lists with different types
print ("\n\n")

# Initialize list
my_list = [["Apple", 3, 6, "String"],["IDK", 10, True, "Meh"],[20, 43, 42, "Yahoo"]]
counter = 0
is_integer = ""

# Find even numbers and add it to counter
for item in my_list:
    for i in item:
        is_integer = isinstance(i, int)
        if is_integer:
            if i % 2 == 0:
                counter += 1

print (counter)
