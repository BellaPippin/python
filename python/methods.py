# This program creates a class and explores methods.
print ("\n\n")

class Pet:

    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getters and Setters
        
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
        
    def get_name(self):
        return self.__name
    
    def set_kind(self, value):
        self.__kind = value
    
    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value
        
    def print_details(self):
        print (self.__name)
        print (self.__kind)
        print (self.__breed)



def main():

    # Create 3 pets

    pet1 = Pet("Cat", "Tabby", "Selina Kyle")
    pet2 = Pet("Cat", "Domestic Longhair", "Dracula")
    pet3 = Pet("Cat", "Maine Coon Mix", "Mr. Sprinkles")

    # Display Pet Details

    pet1.print_details()
    print ("\n")
    pet2.print_details()
    print ("\n")
    pet3.print_details()
    print ("\n")

    # Demonstrate Methods

    print ("\nIs pet1 an instance of the class 'Pet'?")
    print (isinstance(pet1, Pet))

    print ("\nShow the class used to instantiate pet3:")
    print (type(pet3))

    print ("\nAccess breed attribute of object pet3:")
    print (getattr(pet3, "_Pet__breed"))









main()