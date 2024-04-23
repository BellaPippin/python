# Processing sales.txt and displaying its info


def main():
    try:
        # Variables to add total and count lines
        total = 0
        total_lines = 0
        
        with open("sales_totals.txt", 'r') as accounts:
            for line in accounts:
                line = float(line.rstrip('\n'))
                print(f"\n{line}")
                total += line
                total_lines += 1

        """ I learned from ChatGPT (it did not write this code though!) that when we use the "with open" statement Python implicity closes the file to prevent errors so I haven't explicitly closed it here.   """     
        
        # Display totals and average
        print ("\n")
        print ("#" * 10)
        print (f"Total Entries: {total_lines}")
        print(f"Total Sales: {total:,.2f}")
        print (f"Average Sale: {total/total_lines:.2f}")
        print ("\n")


    except IOError:
        print("An IOError has occurred.")



main()
