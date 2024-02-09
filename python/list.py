# This program calculates average steps per week.
print ("\n\n\n")


# Create the lists.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

steps = []

total_steps = 0

# Ask user for input.
for day in days:
    step_count = int(input(f"How many steps did you take on {day}? "))

    steps.append(step_count)
    total_steps = total_steps + step_count

# Print daily steps.   
print ("\n\n")
    
for i in range(len(days)):
    day = days[i]
    step = steps[i]

    print (f"You took {step} steps on {day}.")


# Total Steps.
print ("\n\n")
print (f"You took {total_steps} steps this week.")


# Average Steps.
print ("\n\n")
average = round(total_steps / len(steps))
print (f"Your average steps for this week is {average:.2f}.\n\n")