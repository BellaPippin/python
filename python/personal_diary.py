# This program creates a file for a personal diary and allows the user to add entries to it.
print ("\n\n")

# Function to show file's contents so far
def open_file():
    try:
        # Open the file in read mode
        directory = open('diary.txt', 'r')
        content = directory.read()
        print(content)
        directory.close()  
        return (content)
    except FileNotFoundError:
        print("File not found.")

    except IOError:
        print("We created this file for you, it did not exist or was empty.")

    except Exception as e:
        print("An error occurred:", e)

# Function to write file
def add_values(my_values):
    date = input("What is today's date: ")
    journal = input("Write your journal entry here: ")
    entry = date + ", " + journal + "\n"
    record = open('diary.txt', 'a')
    record.write(entry)
    record.close()
    print ("Entry added successfully!")


def main():
    
    print(f"Welcome to your virtual personal Diary! \n")

    values = open_file()
    add_values(values)

    


main()