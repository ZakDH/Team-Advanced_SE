from bank import Bank

def main():
    # Encapsulation: The Bank object is encapsulated within the main function
    bank = Bank()

    while True:
        print("What service do you wish to use?")
        print("1. Create an account")
        print("2. Deposit into account")
        print("3. Withdraw from account")
        print("4. Transfer between accounts")
        print("5. View account details")
        print("6. Quit")

        validChoice = lambda x: x.isdigit() and 1 <= int(x) <= 6
        choice = input("Enter your choice: ")
        while not validChoice(choice):
            print("Invalid choice...")
            choice = input("Enter your choice: ")

        if choice == "1":
            firstName = input("What is your first name?: ")
            lastName = input("What is your last name?: ")
            # Polymorphism: The createAccount method is called on the Bank object,
            # which can create different types of accounts based on the arguments passed in
            bank.createAccount(firstName, lastName)
                
        elif choice == "2":
            accountNumber = input("Enter account number: ")
            account = bank.getAccount(accountNumber)
            if account:
                depositAmount = input("Please enter deposit amount:" )
                while not depositAmount.isdigit():
                    print("Invalid amount... ")
                    depositAmount = input("Please enter deposit amount:" )
                # Encapsulation: The deposit method is called on the Account object,
                # which is encapsulated within the Bank object
                account.deposit(float(depositAmount), accountNumber)
            else:
                print("Account has not been found...")
                
        elif choice == "3":
            accountNumber = input("Enter account number: ")
            account = bank.getAccount(accountNumber)
            if account:
                withdrawAmount = input("Please enter withdrawal amount:" )
                while not withdrawAmount.isdigit():
                    print("Invalid amount... ")
                    withdrawAmount = input("Please enter withdrawal amount:" )
                try:
                    # Encapsulation: The withdraw method is called on the Account object,
                    # which is encapsulated within the Bank object
                    account.withdraw(float(withdrawAmount), accountNumber)
                except ValueError as e:
                    print(str(e))
            else:
                print("Account has not been found...")

        elif choice == "4":
            accountFrom = input("Enter the account number you want to transfer funds from: ")
            accountTo = input("Enter the account number you want to transfer funds to: ")
            transferAmount = input("Enter amount to transfer: ")
            while not transferAmount.isdigit():
                print("Invalid amount... ")
                transferAmount = input("Enter amount to transfer: ")
            try:
                # Polymorphism: The transfer method is called on the Bank object,
                # which can transfer funds between different types of accounts
                bank.transfer(accountFrom, accountTo, float(transferAmount))
            except ValueError as e:
                print(str(e))
        
        elif choice == "5":
            accountNumber = input("Enter account number: ")
            # Inheritance: The viewDetails method is inherited from the Account class
            # and is called on the appropriate Account object
            bank.viewDetails(accountNumber)
            
        elif choice == "6":
            print("Exiting program...")
            break

if __name__ == '__main__':
    main()
