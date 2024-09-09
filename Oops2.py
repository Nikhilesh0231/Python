#Abstraction and Encapsulation 

class Car :
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False
  def Start(self):
    self.clutch = True
    self.acc = True
    print("Car Started....")

car1 = Car()
car1.Start();

# practice Question

#Create Account Class with two attributes - balance & Account No.
#Create Methods for debit,credit&printing the balance

class Account:
  def __init__(self,account_no,balance):
    self.account_no = account_no
    self.balance = balance
  def debit(self,amt):
    if self.balance >= amt:
      self.balance = self.balance - amt
      print("Debit Successful")
    else:
      print("Insufficient Balance")
  def credit(self,amt):
    self.balance = self.balance + amt
    print("Credit Successful")
  def print_balance(self):
    print("Account No:",self.account_no)
    print("Balance:",self.balance)

a1 = Account(540000,100000)
a1.print_balance()
a1.debit(50000)
a1.print_balance()
a1.credit(602341)
a1.print_balance()
a1.debit(5000098326)
a1.print_balance()