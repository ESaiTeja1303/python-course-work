class BankAccount:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"Balance: {self.balance}")

acc=BankAccount("Arjun")
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()
