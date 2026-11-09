class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def can_withdraw(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Cannot widthdraw a non positive amount of money ")
            return False
        
        if amount > self.balance:
             print("Nedostatek prostředků")
             return False
    
        self.balance -= amount

    def describe(self):
        return f"{self.owner}: {self.balance:.2f} CZK"



acc = BankAccount("Jana")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(5000)      
print(acc.describe()) 