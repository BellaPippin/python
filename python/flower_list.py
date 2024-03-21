# This program manages a list of flowers.
print ("\n\n")

def main():
    
    list = []

    # Add flowers user enters to list until they type "done".
    while True:
        item = input ("Enter your flowers one by one, type 'done' to finish. ")

        if item == "done":
            break
        else:
            list.append(item)
            continue
    
    list.sort()

    index = 1

    # Print sorted list with a number
    for i in list:
        print (f"{index} - {i}")
        index += 1

    

    # Find if flower in list
    while True:
        try:
            search_term = input("\nWhich flower do you wish to search for? ")

            if search_term in list:
                print ("Flower found!")
                break
            else:
                print ("That flower is not on the list.")

        except:
            print ("Something went wrong.")


    while True:
        try:
            number_term = int(input("\nSelect a number to access a flower."))

        # Access flower by number
        
            if number_term > 0:
                print(f"You selected {list[number_term - 1]}")
                break
            else:
                print ("Don't enter negative numbers!")
            
        except IndexError:
            print ("That's not a valid number in the list.")
        except ValueError:
            print ("That's a ValueError, dawg.")
        except: 
            print ("Something went wrong.")

    print ("\nCongrats! You reached the end of the program.")

        







main()