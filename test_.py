import unittest

class TestBank(unittest.TestCase):
    
    def test_deposit(self):
        # Set up any necessary data or objects
        account_balance = 100
        
        # Perform the action you want to test
        deposit_amount = 50
        account_balance += deposit_amount
        
        # Assert that the expected result has occurred
        self.assertEqual(account_balance, 150)
    
    def test_withdraw(self):
        # Set up any necessary data or objects
        account_balance = 100
        
        # Perform the action you want to test
        withdrawal_amount = 50
        account_balance -= withdrawal_amount
        
        # Assert that the expected result has occurred
        self.assertEqual(account_balance, 50)

if __name__ == '__main__':
    unittest.main()
