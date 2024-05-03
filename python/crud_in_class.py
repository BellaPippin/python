"""
    CRUD application for creating an address book.
    This will have some problems in it. you may solve the problems 
    for extra credit:
    Does not allow for duplicate names to be properly handled
    Search searches the entire entry not a specific field


    🚨 Avoid project creep!


"""


def main_menu():
    # present menu
    # Check values 
    # return choice
    try:
        print("\nMain Menu - Customer Directory")
        print("1. Create new entry")
        print("2. Read and display by name")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Quit")
        choice = int(input("Please enter the number of your selection: "))
        if choice < 0 or choice > 5:
            print("That is out of range, please try again.")
            main_menu()
        else:
            return choice
    except ValueError:
        print("That is not a valid number. Please try again.")
        main_menu()
    except Exception as e:
        print(f"main_menu: {e}")

def check():
    # read file to list
    # if file not there create empty customer list
    # return customer list
    try:
        file = open("customer_list.txt", "r")
        customer = file.readlines()
        # for line in customer:
        #     # print(line) # This was for test purposes!
        file.close()
        return customer
    except FileNotFoundError:
        print("That file does not exist. \n We will create a new file for you!")
        customer = []
        return customer
    except Exception as e:
        print(f"Check: {e}")
    

def save(output):
    try:
        # save the file
        file = open("customer_list.txt", 'w')
        for line in output:
            file.write(line)
        file.close()
        print("\nFile updated.")
        main()

    except Exception as e:
        print (f"Save: {e}")

def create():
    # create a new entry
    # call the save  function
    try:
        customer = check()
        print("\n Please enter the customer information: ")
        first_name = input("First name: ")
        last_name = input("Last Name: ")
        phone = input("Phone number: ")
        email = input("Email address: ")
        entry = f"{first_name}, {last_name}, {phone}, {email}\n"
        customer.append(entry)
        # for line in customer:
        #     print(line)
        save(customer)

    except Exception as e:
        print(f"Create: {e}")

    main()

def read():
    # will call the search function
    # will display the found record

    # grab returned list of matching records and display with their indices. 

    try:
        matching_records = search()

        print ("\n**Matching entries:**\n")
        for index, record in enumerate(matching_records):
            print (f"{index + 1}- {record}") # Add 1 to the indices so it doesn't start from 0. Looks ugly.

        # for i in matching_indices:
        #     print (i)

        #print (f"Found {found_customer} at index {found_index}")

    
    except Exception as e:
        print(f"Read: {e}")

    main()

def search():

    # Define a list of matching records. Instead of returning the first found,
    # add record to list and return that list instead.
    # If list is empty, print that the search term wasn't found. (So it doesn't print the message on each line
    # that does not contain the search term)

    try:
        customer = check()

        search_term = input("Enter the last name of the person we should search: ")

        matching_records = []

        for line in customer:

            if search_term in line:
                matching_records.append(line)

        if matching_records == []:
            print (f"{search_term} was not found.")
            
        return matching_records
        
    
    except Exception as e:
        print(f"Search: {e}")


def update():
    # updates a record
    # uses search function
    try:
        # Use search function to return list of matching entries.  
        matching_records = search()

        print ("\n**Matching entries:**\n")
        for index, record in enumerate(matching_records):
            print (f"{index + 1}- {record}")

        index_number = int(input("Enter the number of the record you would like to update: "))

        #print (f"\nRecord selected: {matching_records[index_number - 1]}\n")

        record_to_update = matching_records[index_number - 1].split(', ')

        first_name = record_to_update[0]
        last_name = record_to_update[1]
        phone_number = record_to_update[2]
        email = record_to_update[3]

        print("1: " + first_name + "\n2: " + last_name + "\n3: " + phone_number + "\n4: " + email )

        choice  = int(input("Enter the number of the value that you want to change: "))

        if choice == 1:
            first_name = input("Please enter the new first name: ")
        elif choice == 2:
            last_name = input("Please enter the new last name: ")
        elif choice == 3: 
            phone_number = input("Please enter a new phone number: ")
        elif choice == 4: 
            email = input("Please enter a new email:  ")

        
        # Need to get customer's index!!! AAAAAAAAAA 
        
        customer = check()


        # Compare if the record chosen to update is in the original customer list,
        # when found, get the index of that record.
        # This kept me up at night. :(

        for index, record in enumerate(customer):
            # Convert each line to a list for comparison
            record_as_list = record.split(', ')
            if record_as_list == record_to_update:
                # print(f"{record_to_update} matches {record}")
                # print(f"Index is: {index}")
                break

        del customer[index] # Delete the record to update from the original customer list.

        # Save new entry using the given input
        entry = (first_name + ", " + last_name + ", " + phone_number + ", "  + email)
        customer.append(entry)
        save(customer)


    except Exception as e:
        print(f"Update: {e}")

    main()

def delete():
    # calls search
    # verifies that it is the record to delete
    # deletes the record
    try:
        # Use search function to return list of matching entries.  
        matching_records = search()

        print ("\n**Matching entries:**\n")
        for index, record in enumerate(matching_records):
            print (f"{index + 1}- {record}")

        index_number = int(input("Enter the number of the record you would like to delete: "))

        #print (f"\nRecord selected: {matching_records[index_number - 1]}\n")

        record_to_delete = matching_records[index_number - 1]

        choice = input(f"Do you REALLY wish to delete {record_to_delete}? y/n: ")

        if choice == 'y':

            customer = check()


            # Compare if the record chosen to update is in the original customer list,
            # when found, get the index of that record.

            for index, record in enumerate(customer):
                # Convert each line to a list for comparison
                record_as_list = record.split(', ')
                if record_as_list == record_to_delete:
                    # print(f"{record_to_delete} matches {record}")
                    # print(f"Index is: {index}")
                    break

            del customer[index] # Delete the record to delete from the original customer list.

            print ("Record deleted.")

            save(customer)


        elif choice == 'n':
            print ("Operation cancelled.")
            main()
        
        else:
            print ("That's not a valid answer.")
            main()



    
    except Exception as e:
        print(f"Delete error: {e}")

    main()



def main():
    choice = main_menu()
    try:
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            print("\nGoodbye!\n")
    except Exception as e:
        print(f"Main: {e}")

main()