from bank import Bank

def main():
    bank = Bank()
    while True:
        print("What service do you wish to use?")
        print("1. Create an account")
        print("2. Deposit into account")
        print("3. Withdraw from account")
        print("4. Transfer between accounts")
        print("5. View account details")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            firstName = input("What is your first name?: ")
            lastName = input("What is your last name?: ")
            bank.createAccount(firstName, lastName)
                
        elif choice == "2":
            accountNumber = input("Enter account number: ")
            account = bank.getAccount(accountNumber)
            if account:
                depositAmount = float(input("Please enter deposit amount:" ))
                account.deposit(depositAmount)
            else:
                print("Account has not been found...")
                
        elif choice == "3":
            accountNumber = input("Enter account number: ")
            account = bank.getAccount(accountNumber)
            if account:
                withdrawAmount = float(input("Please enter withdrawal amount:" ))
                account.withdraw(withdrawAmount)
            else:
                print("Account has not been found...")

        elif choice == "4":
            accountFrom = input("Enter the account number you want to transfer funds from: ")
            accountFrom = bank.getAccount(accountFrom)
            if accountFrom:
                accountTo = input("Enter the account number you want to transfer funds to: ")
                accountTo = bank.getAccount(accountTo)
                if accountTo:
                    amount = float(input("Enter amount to transfer: "))
                    accountFrom.transfer(amount, accountTo)
                else:
                    print("Recipient account has not been found...")
            else:
                print("Account has not been found...")
        
        elif choice == "5":
            accountNumber = input("Enter account number: ")
            bank.viewDetails(accountNumber)

        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()