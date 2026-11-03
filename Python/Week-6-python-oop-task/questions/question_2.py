
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance

    def deposit(self,amount):
        # validate the amount 
        if amount <= 0:
            print( f"invalid trnasaction:deposit amount {amount} must be greater than 0")
            return
        # if amount validation pass add the amount to balance
        self.__balance += amount
        print(f"successfully deposited {amount}$")

    def withdraw(self,amount):
        # validate the amount
        if amount <= 0:
            print(f"Invalid transaction:withdrawal amount {amount} must be greater than zero")
            return
        if amount >= self.__balance:
            print(f"Invalid transaction:withdrawal failed.insufficient balance")
            return
        self.__balance -= amount
        print(f"successfully withdraw {amount}")


    def get_balance(self):
         print(f"current balance is {self.__balance}")

        


account1 = BankAccount("Musa", 5000)

# tast valid & invalid transaction
account1.deposit(500)
account1.deposit(-200)
account1.deposit(0)
account1.withdraw(234)
account1.withdraw(0)
account1.withdraw(5000)

account1.get_balance()
