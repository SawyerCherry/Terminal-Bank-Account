import random
def generateAccountNum():
        number = random.randint(10000000, 99999999)
        return number

class BankAccount():
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance


    def deposit(self, amount):
        # originally 0 but change it when you deposit amount
        self.balance += amount 
        print(f'Amount Deposited: ${amount} \n Your balance is ${self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            
            self.balance -= amount
            print(f"You have withdrawn ${amount}. Your updated balance is ${self.balance}")
        else:
            self.balance -= 10
            self.balance -= amount

            #this should charge you 10 dollars when you overdraft #thanksAsIfIWeren'tAlreadyBroke
            #prints out a message

            return print(f"{self.full_name}, you have Insufficient Funds, we have charged you $10 for an overdraft fee. You're  Welcome! \n Your updated balance is ${self.balance}")


    def get_balance(self):
        return f'Your balance is ${self.balance}.'

    def print_receipt(self, full_name, account_number, routing_number, balance):
        print("----------------------")
        print(f"Name: {self.full_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Routing Number: {self.routing_number}") 
        print(f"Balance: ${self.balance}")
        return "----------------------"

    def addInterest(self):
        interest = self.balance *  0.00083 
        self.balance += interest
        return f"Interest has been added, your updated balance is ${self.balance}"
        
routing_num = 349259085

initial_balance = 0

test_account = BankAccount("Sawyer Cherry", generateAccountNum(), routing_num, initial_balance)

test_account.deposit(1000)
test_account.deposit(1000)

#test_account.withdraw(3000)

#print(test_account.get_balance())

#print(test_account.addInterest())

print(test_account.print_receipt("Sawyer Cherry", test_account.account_number, routing_num, test_account.get_balance()))
      