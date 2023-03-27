# Encapsulated class that defines a bank account
class Account:
    def __init__(self, firstName, lastName, accountNumber, balance=0):
        # Encapsulated instance variables
        self.accountNumber = accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        
    # Encapsulated method that returns the account number
    def getAccountNumber(self):
        return self.accountNumber

    # Encapsulated method that deposits funds into the account
    def deposit(self, amount, account):
        self.balance += amount
        print(f"Deposit of {amount:.2f} to {account} was successful.\nNew balance is: {self.balance:.2f}")

    # Encapsulated method that returns the account balance
    def checkBalance(self):
        return self.balance
    
    # Encapsulated method that withdraws funds from the account
    def withdraw(self, amount, account):
        if self.balance < amount:
            raise ValueError(f"Withdrawal of {amount:.2f} failed. Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal of {amount:.2f} from {account} was successful.\nNew balance is: {self.balance:.2f}")
    
    # Encapsulated method that returns the account number as a string
    def __str__(self):
        return self.accountNumber
