# This program calculates BMI.
print ("\n\n")

# Global variables
kg_ratio = 0.453592
mt_ratio = 0.0254


def kg_converter(weight):
    return weight * kg_ratio
    
def mt_converter(height):
    return height * mt_ratio  

def bmi_calc(weight, height):
    return  weight / (height * height)


def main ():
    print ("Hello! This is a BMI calculator.")
    weight = float(input("Please enter your weight in pounds. "))
    height = float(input("Now please enter your height in inches:  "))
    

    bmi = bmi_calc(kg_converter(weight), mt_converter(height))

    print (f"\nYour BMI is {bmi:.2f}\n")

    if bmi < 18.5:
        print("Your are in the underweight category.")
    elif bmi < 24.9:
        print ("You are in the normal weight category")
    elif bmi < 29.9:
        print ("You are in the overweight category")
    else:
        print ("You are in the obese category")

    print ("\n\n\n")

    


main ()