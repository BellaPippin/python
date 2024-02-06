#This program converts numeric grades into letter grades.

# Print n's to separate from garbage
print ("\n\n\n")

# Request the grade
grade = int(input("Enter numeric grade to convert:"))

# It's checkin' time

# Below 60 it's an F
if grade < 60:
        print ("Oh no, your grade is an F. What happened?")
# 60-69 is a D
elif grade < 69:
        print ("Your grade is a D. Phew, barely made it!")
# 70-79 is a C
elif grade < 79:
        print ("Your grade is a C. Good job! There's room for improvement.")
# 80-89 is a B
elif grade < 89:
        print ("Your grade is a B. Great job!")
# 90-100 is an A
elif grade <= 100:
        print ("You got an A! Congrats!")
# Fallback for numbers not between 1-100
else:
        print ("Something went wrong. Try again.")

print ("\n\n\n")