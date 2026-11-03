# Create a Python class named BankAccount.
# Your class should contain:
# A private attribute named __balance.
# A public attribute named account_holder.
# A method named deposit(amount) to add money.
# A method named withdraw(amount) to withdraw money.
# A method named get_balance() to display the current balance.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        