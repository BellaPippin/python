# Create a bank account class to practice. By ChatGPT.
print ("\n\n")

class BankAccount:

    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def get_info(self):
        return f"\nAccount #: {self.account_number}, Balance: {self.balance}\n"

    def deposit(self, amount):
        self.balance += amount
        return f"Balance is now {self.balance}"
    
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Balance is now {self.balance}"
        else:
            print ("Insufficient Funds")

    



def main():

    account1 = BankAccount("3838383838", 200)

    print (account1.get_info())

    print (account1.deposit(500))

    print (account1.withdrawal(300))

main()