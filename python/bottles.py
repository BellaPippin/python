# Let's sing
print ("\n\n\n")

count = 100
while count > 0:
    print(f"{count} bottles of beer on the wall")
    print(f"{count} bottles of beer")
    print("Take one down, pass it around")
    print(f"{count - 1} bottles of beer\n\n")
    count -= 1  # Decrease
if count == 1:
    print(f"{count} bottle of beer on the wall")
    print(f"{count} bottle of beer")
    print("Take one down, pass it around")
    print(f"{count - 1} bottles of beer\n\n")
