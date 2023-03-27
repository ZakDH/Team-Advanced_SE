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

# Subclass of Account that represents a savings account
class SavingsAccount(Account):
    def __init__(self, firstName, lastName, accountNumber, balance=0):
        # Call the constructor of the parent class
        super().__init__(firstName, lastName, accountNumber, balance)
        
    # Override the deposit method to apply interest to the balance
    def deposit(self, amount, account):
        # Calculate interest
        interest = amount * 0.01
        
        # Add the deposit amount and interest to the balance
        self.balance += amount + interest
        
        # Print a message to confirm the transaction
        print(f"Deposit of {amount:.2f} to {account} was successful.\nNew balance is: {self.balance:.2f} (including {interest:.2f} interest)")

# Example code that demonstrates polymorphism
def makeDeposit(account, amount):
    # Call the deposit method of the account object
    account.deposit(amount, account.getAccountNumber())

# Create instances of both Account and SavingsAccount
account1 = Account("John", "Doe", "12345678", 1000.00)
account2 = SavingsAccount("Jane", "Doe", "87654321", 500.00)

# Call the makeDeposit function with both account objects
makeDeposit(account1, 500.00) # Output: Deposit of 500.00 to 12345678 was successful. New balance is: 1500.00
makeDeposit(account2, 500.00) # Output: Deposit of 500.00 to 87654321 was successful. New balance is: 555.00 (including 5.00 interest)
