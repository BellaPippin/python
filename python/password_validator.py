# This program validates passwords.
print("\n\n")

def main():

    valid = False

    while not valid:
            try:
                valid = True   # This will be False if any requirements are not met.
                print("""Password Requirements:\n
                Between 8 to 20 characters long.\n
                Contains at least one uppercase letter.\n
                Contains at least one lowercase letter.\n
                Includes at least one number.\n
                Includes at least one symbol from the set: !@#$%&*\n""")
                
                password = input("Please enter a password that meets the criteria:")
    
            
                if 7 < len(password) < 21:
                     valid = True
                else:
                     valid = False
                     print ("Password is not the right length!")

                

                
                
                        
                   
            

                
                
            except:
                print("Whoops, something went totally wrong...")







main()