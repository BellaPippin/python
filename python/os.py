# Creating and organizing folders using OS module
print("/n/n")

import os

def main():
    try:
        # Create a main folder
        os.mkdir("codequack")

        # Create subfolders
        os.mkdir("codequack/html_hatchlings")
        os.mkdir("codequack/python_pond")
        os.mkdir("codequack/java_joy")

        # A third level of folder
        os.mkdir("codequack/python_pond/quackscripts")
        
    except:
        print ("Woah something happened, and this isn't descriptive at all, is it.")
    else:
        print ("We did it!")
    finally:
        print ("End of program.")



# Call main, because of reasons
main()