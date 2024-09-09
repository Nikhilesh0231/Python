print(1+2)#3 #Addition
print("Hello"+"World")#HelloWorld#Concatenation
print([1,2,3,4]+[5,6,7])#[1, 2, 3, 4, 5, 6, 7]#Merging
#here due to different data types addition operator overladed, working on different data types it behaves in different forms but all this done python it self and known as implicit overloading.

class Complex:
  def __init__(self,real,imag):
    self.real=real
    self.imag=imag
  def showNumber(self):
    print(self.real,"i+",self.imag,"j")
  # def add(self,num2):
  #   newReal = self.real + num2.real
  #   newImag = self.imag + num2.imag
  #   return Complex(newReal,newImag)#This will work on adding like num3 = num2.add(num1)

  def __add__(self,num2):
    newReal = self.real + num2.real
    newImag = self.imag + num2.imag
    return Complex(newReal,newImag)

  def __sub__(self,num2):
    newReal = self.real - num2.real
    newImag = self.imag - num2.imag
    return Complex(newReal,newImag)

num1 = Complex(2,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num2+num1
num3.showNumber()

num3 = num2-num1
num3.showNumber()