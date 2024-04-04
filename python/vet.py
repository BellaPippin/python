# This program creates a class for a pet at the Vet office.
print ("\n\n")

class Pet:

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
    def print_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)
        print("\n\n")
        
    




def main():
    
    # Making 3 objects
    pet1 = Pet("Maria", "Cosenza", "001234", "Selina Kyle", "Cat")
    pet2 = Pet("Juan", "Arredondo", "002345", "Dracula", "Cat")
    pet3 = Pet("Lionel", "Arredondo", "003456", "Mr. Sprinkles", "Cat")

    print ("Welcome to the patient database\n")
    print ("Loading existing patients details...\n")

    # Display patient info
    pet1.print_info()
    pet2.print_info()
    pet3.print_info()

    # Use setter methods
    print ("#" * 10)

    pet3.set_pet_id ("004567")
    print ("ID changed:")
    pet3.print_info()

    # Check Property

    print ("Is there a pet id for Selina Kyle:")
    






main()