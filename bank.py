import random
from account import Account

class Bank:    
    def __init__(self):
        self.__accounts = {}

    def createAccount(self, firstName, lastName):
        accountNumber = str(random.randint(100000, 999999))
        self.__accounts[accountNumber] = Account(accountNumber)
        print(f"Account created for {firstName} {lastName} with the account number {accountNumber}")

    def getAccount(self, accountNumber):
        return self.__accounts.get(accountNumber)

    def viewDetails(self, accountNumber):
        account = self.__accounts.get(accountNumber)
        if account:
            print(account)
        else:
            print("Account not found.")