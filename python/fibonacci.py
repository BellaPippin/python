# This program produces the Fibonacci sequence. Exercise given by ChatGPT.
print("\n\n")

def main():

    current_number = 0  # Start with 0
    next_number = 1  # Next number after 0 is 1
    print(current_number)  # Print the first Fibonacci number
    for i in range(19):  # Since we printed the first number, we iterate 19 more times to get 20 numbers in total
        print(next_number)
        current_number, next_number = next_number, current_number + next_number

main()