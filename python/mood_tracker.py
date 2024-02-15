# This program tracks the user's moods over the course of a week. (Nested list practice)
print ("\n\n")

# Initialize list of days, list of moods
days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday", "Sunday"]
moods = []

# Get user input
for day in days:
    mood = input(f"What was your mood on {day}? ")
    moods.append([day, mood])

print ("\nFantastic! Let's see how this week went:\n")

for mood in moods:
    print (mood[0],": ", mood[1])
    print ("\n")