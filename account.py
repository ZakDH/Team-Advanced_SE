class Account:
    def __init__(self, firstName, lastName, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        
    def getAccountNumber(self):
        return self.accountNumber

    def deposit(self, amount, account):
        self.balance += amount
        print(f"Deposit of {amount:.2f} to {account} was successful.\nNew balance is: {self.balance:.2f}")

    def checkBalance(self):
        return self.balance
    
    def withdraw(self, amount, account):
        if self.balance < amount:
            raise ValueError(f"Withdrawal of {amount:.2f} failed. Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal of {amount:.2f} from {account} was successful.\nNew balance is: {self.balance:.2f}")
    
    def __str__(self):
        return self.accountNumber