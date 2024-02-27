# This program calculates BMI.
print ("\n\n")

# Global variables
KG_RATIO = 0.453592
MT_RATIO = 0.0254


def kg_converter(weight):
    return weight * KG_RATIO
    
def mt_converter(height):
    return height * MT_RATIO  

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