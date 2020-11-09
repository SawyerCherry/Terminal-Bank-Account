# Some Code

class BankAccount():
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance


    def deposit(self, amount):
        # originally 0 but change it when you deposit amount
        self.balance = self.balance + amount 

    def withdraw(self, amount):
        if self.balance >= amount:
            #this should charge you 10 dollars when you overdraft #thanksAsIfIWeren'tAlreadyBroke
            self.balance -= amount
        else:
            self.balance = amount - 10

            #prints out a message

            print(f"{full_name}, you have Insufficient Funds, we have charged you $10 for an overdraft fee. You're  Welcome!")

    def print_receipt(self, full_name, account_number, routing_number, balance):
        return self.balance



        
            

    
            
        








    
