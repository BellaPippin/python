# This Gen-Z Computer will compare two numbers. Inspired by how my step-son talks.
print ("\n\n\n")

# Ask for numbers.
a = int(input("Can I get a number? "))
b = int(input("Bet. Can I get another number? "))

print ("\nAight. Let me compare.\n")
print (10 * "*")
print ("\n\n")

# Compare.

if a > 50 and b > 50:
    print ("Both numbers are greater than 50. No cap.\n")
else:
    print ("One or more numbers are not greater than 50. No cap.\n")
           
if a > 200 and b > 200:
    print ("You chose both numbers to be greater than 200 frfr.\n")
else:
    print ("One or more numbers are smaller than 200 frfr.\n")

if a % 2 == 0 or b % 2 == 0:
    print ("Aight bet. At least one number is even.\n")
else:
    print ("Both numbers are odd. That is fire.\n")

if a == 40 or b == 40:
    print ("Wow you chose 40 for one or both of your numbers. Fire.\n")
else:
    print ("None of your numbers is equal to 40. Fr.\n")

if a != b:
    print ("Aight you chose two different numbers!\n")
else:
    print ("Wow you wrote the same two numbers.\n")

if a != 10:
    print ("No cap you chose 10 as one of you numbers.\n")
else:   
    print ("No cap your first number is equal to 10\n")


print ("Alr goodbye.\n")