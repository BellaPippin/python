"""
Welcome! This program converts kilograms to pounds.

"""
print("\n\n\n\n")

# Conversion Factor: Pounds (lb) = Kilograms (kg) * 2.20462
conversion_factor = 2.20462

# First we set up some initial values in some variables. (This is how I'd talk to a rubber duck.)
kg_value_1 = 70
kg_value_2 = 50
kg_value_3 = 30.8
kg_value_4 = 100
kg_value_5 = 120

# Now the math: 

lbs_value_1 = kg_value_1 * conversion_factor
lbs_value_2 = kg_value_2 * conversion_factor
lbs_value_3 = kg_value_3 * conversion_factor
lbs_value_4 = kg_value_4 * conversion_factor
lbs_value_5 = kg_value_5 * conversion_factor

# Now we show it: 

print(f"{kg_value_1} kilograms is {lbs_value_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is {lbs_value_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is {lbs_value_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is {lbs_value_4:.2f} pounds.")
print(f"{kg_value_5} kilograms is {lbs_value_5:.2f} pounds.")

print("\n\n\n\n")
