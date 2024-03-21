# This program handles a list of artists.
print ("\n\n")

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    print ("These are the top ten performing artists of all time:")

    index = 0

    for artist in top_artists:
        print (f"{index} - {artist}")
        index +=1
    
    while True: # Ask for a number to replace and artist and new artist. If exception is raised keep trying.
        try:
            index_choice = int(input("\nEnter the number of the artist you would like to replace: "))

            new_artist = input("Enter the name of the new artist:  ")

            top_artists[index_choice] = new_artist

            print (f"\n{new_artist} has been added to the list.") # Operation successful.
            
            index = 0

            for artist in top_artists: # Prrrrrrint
                print (f"{index} - {artist}")
                index +=1

            break

        except ValueError:
            print ("That's not a number. Try again.")
        except IndexError:
            print ("That number is not on the list! Try again.")
        except Exception as e:
            print (f"The following went wrong: {e}. Try again.")


main()