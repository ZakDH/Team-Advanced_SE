import unittest
from account import Account, SavingsAccount

class TestAccount(unittest.TestCase):
    def test_create_account(self):
        account = Account("John", "Doe", "12345678", 1000.00)
        self.assertEqual(account.firstName, "John")
        self.assertEqual(account.lastName, "Doe")
        self.assertEqual(account.accountNumber, "12345678")
        self.assertEqual(account.balance, 1000.00)

    def test_deposit(self):
        account = Account("John", "Doe", "12345678", 1000.00)
        account.deposit(500.00, account.getAccountNumber())
        self.assertEqual(account.balance, 1500.00)

    def test_withdraw(self):
        account = Account("John", "Doe", "12345678", 1000.00)
        account.withdraw(500.00, account.getAccountNumber())
        self.assertEqual(account.balance, 500.00)

    def test_insufficient_funds(self):
        account = Account("John", "Doe", "12345678", 1000.00)
        with self.assertRaises(ValueError):
            account.withdraw(1500.00, account.getAccountNumber())

class TestSavingsAccount(unittest.TestCase):
    def test_create_savings_account(self):
        account = SavingsAccount("John", "Doe", "12345678", 1000.00)
        self.assertEqual(account.firstName, "John")
        self.assertEqual(account.lastName, "Doe")
        self.assertEqual(account.accountNumber, "12345678")
        self.assertEqual(account.balance, 1000.00)
def test_deposit_with_interest(self):
    account = SavingsAccount("John", "Doe", "12345678", 1000.00)
    account.deposit(500.00, account.getAccountNumber())
    self.assertEqual(account.balance, 1505.00)
    account.deposit(500.00, account.getAccountNumber())
    self.assertEqual(account.balance, 1550.00)


if __name__ == '__main__':
    unittest.main()
