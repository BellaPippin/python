# This program counts how many times a specific element appears inside lists.
print ("\n\n")

my_list = [[ 1 , 2 , 3 , 4 , 6 , 8 , 5 ],[ 4 , 5 , 6 , 3 , 8 , 2 , 6 ],[0 , 9 , 3 , 8 , 5 , 2 , 1 , 0 ]]
total_occurrences = 0

# Get user input
print ("Welcome!")
number = int(input("Please enter a number between 1 and 10: "))

# Loop through the list, add 1 to total_occurrences each time item in list

for i in my_list:
    for item in i:
        if number == item:
            total_occurrences += 1

print (total_occurrences)