#  Bank Account Management
# Create a BankAccount class with the following requirements:
# Define attributes: owner and balance.
# Initialize them using __init__().
# Create a deposit(amount) method to increase the balance.
# Create a withdraw(amount) method to decrease the balance.
# Create a display_balance() method to display the current balance.
# Create two bank account objects with different owners and balances.
# Perform multiple deposits and withdrawals on each account.
# Prevent withdrawals when the requested amount is greater than the available balance.
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        # increase account's balance by the amount deposited
    def deposit(self,amount):
     self.balance=self.balance +amount
      

        