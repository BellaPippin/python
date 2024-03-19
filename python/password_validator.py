# This program validates passwords.
print("\n\n")

def main():

    valid = False

    while valid == False:
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
                    print("This password is not the right length!")

                for ch in password:
                    if ch.isupper():
                        continue
                    else:
                        print("There has to be an uppercase character!")
                
            except:
                print("Whoops, something went totally wrong...")







main()