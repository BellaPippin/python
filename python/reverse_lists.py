# Exercise: Reverse a Nested List

# Write a Python program that reverses the order of elements in each sublist of a nested list, while also reversing the order of the sublists themselves. For example, given the nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]], the output should be [[9, 8, 7], [6, 5, 4], [3, 2, 1]].
print ("\n\n")

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for item in nested_list:
   item.reverse()

nested_list.reverse()

print (nested_list) 