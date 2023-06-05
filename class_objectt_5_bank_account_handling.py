#challenge5
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def withdrawl(self, amount):
        self.balance -= amount  
        
    def deposit(self, amount):
         self.balance += amount     
    
    def get_balance(self):
        return self.balance

class savingsAcccount(Account):
    def __init__(self,title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestamount(self):
        interestamount = (self.interestRate * self.balance)/100
        return interestamount
        


object = savingsAcccount("ashish", 2000, 5)
object.deposit(500)
print(object.get_balance())    #balance-2500
object.withdrawl(int(input("enter the amount to withdraw: ")))#2500-withdraw amount
print(f" Available balance left: {object.get_balance()}")    #balance-remaining amount after withdrawal 
print(object.interestamount())  #interest - 100
