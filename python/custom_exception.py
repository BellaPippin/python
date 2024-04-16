# This program raises a custom exception when user inputs something other than a number
print ("\n\n")

class  NotNumericError(ValueError):
    def __init__(self, message="You did not enter a number. Please enter a number!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


def main():
    try:
        # Get input from user
        value = int(input("Please enter a number from 0 to 9: "))
        if not value.isnumeric():
            raise NotNumericError()


    except NotNumericError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"The exception is: {e}")
        main()
    else:
        print(f"Thank you, you entered {value}.")
    finally:
        print("Program ended.")


main()