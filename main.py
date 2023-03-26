import random

class Account:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def checkBalance(self):
        return self.__balance

    
    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient balance, please re-enter a withdrawal amount...")
        self.__balance -= amount

def createAccount(name):
    account_number = str(random.randint(100000, 999999))
    account = Account(account_number)
    print(f"Account created for {name} with the account number {account_number}")
    return account


# Example usage
name = input("What is your first name?: ")
account = createAccount(name)

while True:
    deposit = input("How much do you want to deposit into your new account?: ")
    try:
        intDeposit = int(deposit)
        break;
    except ValueError:
        try:
            float(deposit)
            break;
        except ValueError:
            print("Please enter a valid amount to be deposited...")
account.deposit(intDeposit)
print(account.checkBalance())

while True:
    withdraw = input("How much do you want to withdraw from your new account?: ")
    try:
        intWithdraw = int(withdraw)
        break;
    except ValueError:
        try:
            float(withdraw)
            break;
        except ValueError:
            print("Please enter a valid amount to be deposited...")
account.withdraw(intWithdraw)

deposit = input("How much do you want to deposit into your new account?: ")
deposit = int(deposit)
account.deposit(deposit)

print(account.checkBalance())