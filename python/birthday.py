# This program calculates a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

# Import datetime module
from datetime import datetime

def main():
   
    print("\n\n")
    try:
        today = datetime.today()

        # Ask user to input their birth date
        birth_year = int(input("What year were you born?  "))
        month = int(input("What month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        
        #Make a date object with user's input and display it
        birthday = datetime(birth_year, month, day)
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(f"\nOk. You were born on {birthday_output}.\n") 

        # Do math based on the day difference
        delta = today - birthday
        delta_years = delta.days // 365.2425
        delta_months = delta.days // 12
        delta_weeks = delta.days // 7
        delta_days = delta.days
       
        # Display results
        print (f'You are {delta_years} years old.')
        print (f"That is {delta_months} months!")
        print (f"That is {delta_weeks} weeks!")
        print (f"That is {delta_days} days!")

        print ("\nFeel old yet?\n")

       
      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()