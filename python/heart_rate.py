# This is a program to collect and manage your heart rate.
print ("\n\n")

# Initialize times list, rates list
test_times = ["Morning", "Afternoon", "Evening"]
rates = []
total = 0

# Ask user for rates at different times of day.
for time in test_times:
    heart_rate = int(input(f"Enter your heart rate for {time}: "))
    rates.append([time, heart_rate])
    total += heart_rate # Add the heart rate to the "total" variable for later use

# Print average heart rate for the day    
average = round(total / len(rates))
print("\nYour average heart rate for the day is ", average)