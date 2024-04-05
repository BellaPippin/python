# This is a practice for classes. Make a rectangles class and methods to calculate area of rectangles. Exercise by ChatGPT.
print ("\n\n")

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    # Getters and Setters

    def get_length (self):
        return self.__length
    
    def get_width (self):
        return self.__width
    
    def set_length (self, value):
        self.__length = value

    def set_width (self, value):
        self.__width = value

    def calc_area (self):
        return self.__width * self.__length
    

def main():

    rectangle1 = Rectangle (3, 5)
    rectangle2 = Rectangle (5, 10)
    
    print ("Area of rectangle1:")
    print (rectangle1.calc_area())
    print ("\n")
    print ("Area of rectangle2:")
    print (rectangle2.calc_area())



main()
    
