import unittest
from unittest.mock import patch
from bank import Bank

class TestBank(unittest.TestCase):
    
    def setUp(self):
        self.bank = Bank()
        
    def test_createAccount(self):
        with patch("builtins.print") as mock_print:
            self.bank.createAccount("John", "Doe")
            self.assertEqual(len(self.bank.accounts), 1)
            mock_print.assert_called_with("Account created for John Doe with the account number {}".format(list(self.bank.accounts.keys())[0]))
            
    def test_getAccount(self):
        self.bank.createAccount("John", "Doe")
        account = self.bank.getAccount(list(self.bank.accounts.keys())[0])
        self.assertEqual(account.firstName, "John")
        self.assertEqual(account.lastName, "Doe")
        
    def test_viewDetails(self):
        self.bank.createAccount("John", "Doe")
        with patch("builtins.print") as mock_print:
            self.bank.viewDetails(list(self.bank.accounts.keys())[0])
            mock_print.assert_called_with("--Account Details--\n\nFirst Name: John\nLast Name: Doe\nAccount Number: {}\nBalance: 0.00\n".format(list(self.bank.accounts.keys())[0]))
        with patch("builtins.print") as mock_print:
            self.bank.viewDetails("000000")
            mock_print.assert_called_with("Account not found.")
            
    def test_transfer(self):
        self.bank.createAccount("John", "Doe")
        self.bank.createAccount("Jane", "Doe")
        with patch("builtins.print") as mock_print:
            self.bank.transfer(list(self.bank.accounts.keys())[0], "000000", 1000)
            mock_print.assert_called_with("Account 000000 not found.")
        with patch("builtins.print") as mock_print:
            self.bank.transfer(list(self.bank.accounts.keys())[0], list(self.bank.accounts.keys())[1], 1000)
            mock_print.assert_called_with("Insufficient balance.")
        with patch("builtins.print") as mock_print:
            self.bank.transfer(list(self.bank.accounts.keys())[0], list(self.bank.accounts.keys())[1], 500)
            mock_print.assert_called_with("Transfer of 500.00 from account {} to account {} was successful.\nNew balance in account {} is: 500.00".format(list(self.bank.accounts.keys())[0], list(self.bank.accounts.keys())[1], list(self.bank.accounts.keys())[0]))
            self.assertEqual(self.bank.getAccount(list(self.bank.accounts.keys())[0]).checkBalance(), 0)
            self.assertEqual(self.bank.getAccount(list(self.bank.accounts.keys())[1]).checkBalance(), 500)
