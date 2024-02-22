# This program calculates simple interest
print ("\n\n")

def calc_interest(principal, roi, time):
    total_interest = (principal * roi * time) / 100
    return total_interest



def main():
    print ("Hello there! This is calculator.")
    principal = float(input("Please enter a principal amount:  "))
    roi = int(input("What is the interest rate? "))
    time = int(input("What is the number of years for the loan?  "))

    print(f"\nYour interest is: {calc_interest(principal, roi, time):.2f}")

main ()
