# Getting and displaying calendars from the calendar module
print ("\n\n")

# Import module
import calendar, datetime

def main():

    try:
        
        # Ask user for their birth month
        print ("## Make a Calendar ##")
        month = int(input("What's your birth month (as a number)? " ))
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
            
        
        # Get current year - from https://favtutor.com/blogs/get-current-year-python
        today = datetime.date.today()
        year = today.year

        # Print calendar for user's birth month for this year
        print ("\n")
        print ("Here's a calendar of your birth month for this year!\n")
        print (calendar.month(year, month))

        

    except Exception as e:
        print (f"Oopsie happened: {e}")
        main()



main()