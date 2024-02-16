# Exercise: Flatten a Nested List with Mixed Data Types

# Write a Python program that flattens a nested list containing mixed data types (integers, floats, strings, etc.) into a single-level list. For example, given the nested list [[1, 2, 3], [4.0, 5, "hello"], ["world", 6.5]], the output should be [1, 2, 3, 4.0, 5, "hello", "world", 6.5].

# This exercise requires you to handle the conversion of various data types and flatten the nested list while preserving the original data types of the elements.

print ("\n\n")

# Initialize lists
my_list = [[1, 2, 3], [4.0, 5, "hello"], ["world", 6.5]]
flattened_list = []

# Flatten
for item in my_list:
    for i in item:
        flattened_list.append(i)

print (flattened_list)
