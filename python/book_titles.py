# This program takes book titles and sorts them alphabetically.
print("\n\n")

def main():
    book_list = []

    for i in range (10):     # Ask for 10 titles, convert to lower case for comparison, append to list
        book = input("Enter a book title! ")
        book_lower = book.lower()
        book_list.append(book_lower)


    book_list_sorted = sorted(book_list) # Sort list
    
    print ("\nHere are your books in alphabetical order!\n")
    for book in book_list_sorted: # Re-capitalize each book title
        print(book.title()) #Prrrrrrint



main()