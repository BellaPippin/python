# This program validates passwords.
print("\n\n")

def main():

    valid = False

    while not valid:
            valid = True   # This will be False if any requirements are not met.
            print("""Password Requirements:\n
            Between 8 to 20 characters long.\n
            Contains at least one uppercase letter.\n
            Contains at least one lowercase letter.\n
            Includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*\n""")
             
            password = input("Please enter a password that meets the criteria:")
    
            try:
                if 7 < len(password) < 21:
                     continue
                else:
                     valid = False
                     print ("Password is not the right length!")

                for ch in password:
                     if ch.isupper():
                        continue
                     else:
                        valid = False
                        print ("There has to be an uppercase letter!")

                for ch in password:
                     if ch.islower():
                        continue
                     else:
                        valid = False
                        print ("There has to be a lowercase letter!")

                
                
                        
                   
            

                
                
            except:
                print("Whoops, something went totally wrong...")







main()