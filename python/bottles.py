# Let's sing
print ("\n\n\n")

count = 100
while count > 0:
    if count == 1:
        print(f"{count} bottle of beer on the wall")
        print(f"{count} bottle of beer")
        print("Take one down, pass it around")
        print(f"{count - 1} bottles of beer\n\n")
    else:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer")
        print("Take one down, pass it around")
        print(f"{count - 1} bottles of beer\n\n")
    count -= 1  # Decrease

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    

