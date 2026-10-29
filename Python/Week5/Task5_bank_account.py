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
    def withdraw(self,amount):
       if(amount>self.balance or amount<=0):
          return "insufficent balance"
       else:
        self.balance=self.balance-amount
    def display_balance(self):
       return self.balance
banceAccount1=BankAccount("Zidan",2000)    
banceAccount2=BankAccount("Sara",3000)
# give the deposit amount  to banceAccount1
banceAccount1.deposit(500)
banceAccount2.deposit(500)
# deposit money from Zidan's and sara's bank account
print("================================================")
print("Zidan's balance after deposit:",banceAccount1.display_balance())
print("Sara's balance after deposit",banceAccount2.display_balance())

print('================================================')
print(banceAccount1.withdraw(3000))
banceAccount2.withdraw(200)
print("=================================================")
print("Zidan's final balance:",banceAccount1.display_balance())
print("Sara's final balance:",banceAccount2.display_balance())
       
      

        