#wap to create account class with account and balance as attributes.
class Account:
    def __init__(self, account, balance):
        self.acc = account
        self.bal = balance

        #debit method
    def debit(self , amount):
        self.bal -= amount
        print("Rs.",amount, "debit")

        #credit method
    def credit(self , amount):
        self.bal += amount
        print("Rs.",amount, "credit")
        
acc1 = Account(2000,879)
print(acc1.acc)
print(acc1.bal)
acc1.debit(500)
acc1.credit(1000)