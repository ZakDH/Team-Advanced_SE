import random
from account import Account

class Bank:    
    def __init__(self):
        self.accounts = {}

    def createAccount(self, firstName, lastName):
        accountNumber = str(random.randint(100000, 999999))
        account = Account(firstName, lastName, accountNumber)
        self.accounts[accountNumber] = account
        print(f"Account created for {firstName} {lastName} with the account number {accountNumber}")

    def getAccount(self, accountNumber):
        return self.accounts.get(accountNumber)

    def viewDetails(self, accountNumber):
        account = self.accounts.get(accountNumber)
        if account:
                print("--Account Details--")
                print(f"\nFirst Name: {account.firstName}")
                print(f"Last Name: {account.lastName}")
                print(f"Account Number: {account.getAccountNumber()}")
                print(f"Balance: {account.checkBalance():.2f}\n")
        else:
            print("Account not found.")
    
    def transfer(self, accountNumberFrom, accountNumberTo, amount):
        accountFrom = self.getAccount(accountNumberFrom)
        accountTo = self.getAccount(accountNumberTo)
        if not accountFrom:
            print(f"Account {accountNumberFrom} not found.")
            return
        if not accountTo:
            print(f"Account {accountNumberTo} not found.")
            return
        try:
            accountFrom.withdraw(amount, accountFrom)
            accountTo.deposit(amount, accountTo)
        except ValueError as e:
            print(str(e))