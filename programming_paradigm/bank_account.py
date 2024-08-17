
class BankAccount:
    def __init__(self,balance):
        #  self.balance = 0.0
        self.balance=balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        # self.balance -= withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            return True
        else:
            # print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: $ {self.balance}")
# Account=BankAccount(100)
# Account.withdraw(20)
# Account.display_balance()
# # withdraw_amount=float(input("Please Enter withdraw amount: "))
# deposit_amount=float(input("Please Enter deposit amount: "))
# Account.deposit(deposit_amount)
# Account.display_balance()