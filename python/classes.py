# This program defines a class and does stuff with it
print("\n\n")

# Class definition for Person
class Person:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Getters

    def get_info(self):
        return f"\nThis person is called {self.__name} and lives at {self.__address}, is aged {self.__age} and their phone number is {self.__phone_number}."
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
    # Setters

    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    


def main():

    person1 = Person ("Maria Cosenza", "145 Ridge Ave", "34", "(312) 123-4567")
    person2 = Person ("Some Name", "123 Fake St", "45", "(312) 555-1234")
    person3 = Person ("Ducky McDuckFace", "231 Shady Lane", "23", "(312) 222-2222")

    print (person1.get_info())
    print (person2.get_info())
    print (person3.get_info())

    print("\n\n")

    print (person1.get_name())
    print (person3.get_phone_number())



main()