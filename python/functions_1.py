print("\n\n")

# define functions
def square(side):
    square_area = side * side
    print(f"\nThe area of the square is {square_area}")

def circle(radius):
    circle_area = 3.14 * radius * radius
    print(f"\nThe area of the circle is {circle_area}")   


# take input from user
side = int(input("Enter a number for side measurement:  "))
radius = int(input("Enter a number for a radius measurement:  "))

# call the functions
square(side)

circle(radius)