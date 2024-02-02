# Print a few lines to separate from the garbage
print ("\n\n\n")

# Welcome the user and gather info
print (10 * "*")
print ("Welcome! Let's take a look at your budget. Write 0 for any costs that you don't have.")
print (10 * "*")
print ("\n\n")


total_allowance = float(input ("\nWhat's your monthly income?\n"))

housing = float(input ("\nHow much is your housing cost?\n"))

utilities = float(input ("\nHow much are your utilities?\n"))

groceries = float(input ("\nHow much do you spend on groceries each month?\n"))

transportation = float(input ("\nWhat are your monthly transportation costs?\n"))

healthcare = float(input ("\nIf you have any monthly healthcare costs please enter it now.\n"))

personal_care = float(input ("\nAny monthly personal care costs?\n"))

debt = float(input ("\nWhat are your debt total monthly payments?\n"))


print ("\n\n\n")
print (10 * "*")
print ("Thinking... bear with me")
print (10 * "*")
print ("\n\n")


# Calculation time and display results

print (f"Your total monthly income is  {total_allowance:.2f} \n\n ")


housing_per = (housing / total_allowance) * 100
print (f"Your housing represents {housing_per:.2f} % of your budget.\n\n")

utilities_per = (utilities / total_allowance) * 100
print (f"Your utilities represent {utilities_per:.2f} % of your budget.\n\n")

groceries_per = (groceries / total_allowance) * 100
print (f"Your groceries represent {groceries_per:.2f} % of your budget.\n\n")

transportation_per = (transportation / total_allowance) * 100
print (f"Your transportation costs represent {transportation_per:.2f} % of your budget.\n\n")

healthcare_per = (healthcare / total_allowance) * 100
print (f"Your healthcare costs represent {healthcare_per:.2f} % of your budget.\n\n")

personal_care_per = (personal_care / total_allowance) * 100
print (f"Your personal care costs represent {personal_care_per:.2f} % of your budget.\n\n")

debt_per = (debt / total_allowance) * 100
print (f"Your debt payments represent {debt_per:.2f} % of your budget.\n\n")


# Say goodbye
print ("\n\n\n")
print (10 * "*")
print ("Now start saving!")
print (10 * "*")
print ("\n\n")





