class Student:
  def __init__(self,name):
    self.name = name
    self.age = 17

s1 = Student("Nikhilesh")
print(s1.name,"\n",s1.age)
print(s1)
del s1.name
# print(s1.name,"\n",s1.age)#we get an error that attribute name is not present 

del s1
# print(s1)

#private atrribute and Mrethods

class Account:
  def __init__(self,acc_no,acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass
  def resetPass(self):
    print(self.__acc_pass)


acc1 = Account("1234551","VEeRu123")   
print(acc1.acc_no)
# print(acc1.acc_pass) #Now we cannot access the password because password is private 
acc1.resetPass()



#inheritance 

class Car:
  def __init__(self,type):
    self.type = type
  @staticmethod
  def start():
    print("Car Started...")
  @staticmethod
  def stop():
    print("Car Stopped...")

class MahindraCar (Car):
  def __init__(self,name,type):
    self.name = name
    super().__init__(type)

car1 = MahindraCar("Scorpio","Diesal")
print(car1.name)
print(car1.type)

# class MahindraCar (Car):
#   def __init__(self,brand):
#     self.brand = brand

# c1 = MahindraCar("Scorpio")

# c1.start()
# print(c1.name)

# class Scorpio(MahindraCar):
#   def __init__(self,type):
#     self.type = type

# car1 = Scorpio("Diesal")
# car1.start()



class A:
  varA = "Welcome To Class A"

class B:
  varB = "Welcome To Class B"

class C( A,B):
  varC = "Welcome To Class C"


c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)