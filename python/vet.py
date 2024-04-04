# This program creates a class for a pet at the Vet office.
print ("\n\n")

class Pet:
    # Class variable
    vet_name = "Pet Peeve Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type= "dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getters and Setters
        
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type

    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # Display Info
    def display_pet_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)
        print("\n")

    # Check property function    
    def check_property(self, string):
        return hasattr(self, string)




def main():
    
    # Making 3 objects
    pet1 = Pet("Maria", "Cosenza", "001234", "Selina Kyle", "Cat")
    pet2 = Pet("Juan", "Arredondo", "002345", "Dracula", "Cat")
    pet3 = Pet("Lionel", "Arredondo", "003456", "Mr. Sprinkles", "Cat")

    print ("Welcome to the patient database\n")
    print ("Loading existing patients details...\n")

    # Display patient info
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    # Use setter methods
    print ("#" * 10)

    pet3.set_pet_id ("004567")
    print ("ID changed:")
    pet3.display_pet_info()

    # Check Property. 

    print ("Is there a pet id for Selina Kyle:")
    print (pet1.check_property("_Pet__pet_id"))

    print ("\n")

    print ("Is there an owner last name for Mr Sprinkles:")
    print (pet3.check_property("_Pet__owner_last_name"))

    print ("\n")

    print ("Is there a pet name for Juan's cat:")
    print (pet2.check_property("_Pet__pet_name"))

    print ("\n")

    print ("Is there a breed for Lionel's pet:")
    print (pet2.check_property("_Pet__breed"))



    






main()