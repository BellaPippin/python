"""
This program writes an Employee class and a Production Worker subclass,
asks user for input for an employee and then displays it. 

"""
print ("\n\n")

# This is the superclass
class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    # Getters and Setters
    def get_employee_name(self):
        return employee_name
    
    def get_employee_number(self):
        return employee_number
    
    def set_employee_name(self, value):
        self.employee_name = value

    def set_employee_number(self,value):
        self.employee_number = value

# This is the subclass
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, pay_rate, shift):
        super().__init__(employee_name, employee_number)
        self.pay_rate = pay_rate
        self.shift = shift

    # Getters and Setters
        
    def get_pay_rate(self):
        return self.pay_rate
    
    def get_shift(self):
        return self.shift
    
    def set_pay_rate(self,value):
        self.pay_rate = value

    def set_shift(self, value):
        self.shift = value


def convert_shift(int):
    if int == 1:
        return "Day"
    elif int == 2:
        return "Night"
    else:
        print ("Please enter a valid number")
         
    
def main():
    
    # Ask user for input for each of the employee's details
    print ("## Welcome ##\n")
    input_name = input("Please enter employee's name: ")
    input_employee_number = int(input("Please enter employee's number: "))
    input_pay_rate = float(input("Please enter employee's pay rate: "))
    input_shift = int(input("Enter 1 for day shift, 2 for night shift: "))

    # Convert 1 or 2 into "Day" or "Night"
    word_shift = convert_shift(input_shift)

        

    # Initialize an employee

    employee1 = ProductionWorker(input_name, input_employee_number, input_pay_rate, word_shift)

    # Display Employee Details

    print ("\n## Details of Employee:## \n")

    













main()