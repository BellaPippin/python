# This program takes five names and sorts them.
print ("\n\n")
# Empty list
names = []

# Get five names from user to get on the list.

for i in range (0,5):
    name = input ("Enter a name... ")
    name = name.lower() # Convert to lowercase
    names.append (name) # Append to list

# Do the magic (swap).
swapped = True
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print ("\nAlphabetical order:")            
print(names)
print ("\n\n")

# Reverse the list  
names.reverse()

# Print the reversed list
print ("Reverse Alphabetical order:") 
print(names)
print ("\n\n")