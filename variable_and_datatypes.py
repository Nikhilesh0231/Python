print("nikhilesh tiwari")
print("nikhilesh tiwari")
print("nikhilesh tiwari")
print("nikhilesh tiwari")
print("nikhilesh tiwari")
print(1)
print(2)
print(3)
print(4)
print(5)
print("   ")

print("My name is Nikhilesh Tiwari.","My age us 23","Currently I am writting Python code.")

# variables

name = "Nikhilesh Tiwari"
age = 23
caste = "brahaman"
print(name,age,caste)

age+=2
print(age)

print("My name is ", name , "and my age is " , age , "And i am " , caste) 

age2 = age;
print("Value of age2 :",age2)

print(type(name))
print(type(age))
print(type(caste))

name1 = 'hi'
name2 = "hello"
name3 = '''hey'''
print(name1,name2,name3)


old = False
print(type(old))


v =None
print(type(v))
print(v)

# print the sum of two numbers 

num1 = 19
num2 = 23

sum = num1 + num2

print("The sum of num1 (",num1,") and num2 (",num2,") is : ",sum)


#comments

#single line comment 

"""
multi 
line
comment
"""


#Operators 

#Arithematic Operator

a = 12
b = 6

print("The value of a + b is : ",a+b)
print("The value of a - b is : ",a-b)
print("The value of a * b is : ",a*b)
print("The value of a / b is : ",a/b)
print("The value of a % b is : ",a%b)
print("The value of a ** b is : ",a**b)
print("The value of a // b is : ",a//b)
#Assignment Operator
a += 5
print(a)
a -= 5
print(a)
a *= 2
print(a)
a /= 2
print(a)

a %= 3
print(a)

a **= 2
print(a)
#Comparison Operator

c = 14
d = 15
print("The value of c == d is : ",c==d)
print("The value of c != d is : ",c!=d)
print("The value of c > d is : ",c>d)
print("The value of c < d is : ",c<d)
print("The value of c >= d is : ",c>=d)
print("The value of c <= d is : ",c<=d)

#Logical Operator

#AND Operator
val1 = True
val2 = False
val3 = True
val4 =False
print("The value of val1 and val2 is : ",val1 and val2)#false
print("The value of val1 and val3 is : ",val1 and val3)#true
#OR Operator
print("The value of val1 or val2 is : ",val1 or val2)#true
print("The value of val1 or val2 is : ",val1 or val3)#true
print("The value of val1 or val4 is : ",val1 or val4)#true
print("The value of val1 or val4 is : ",val2 or val4)#false

#NOT Operator
print(not True);#false
print(not False);#true


#typeConversion 

f = 34
g = 32.2

i = f + g #34.0 + 32.2
print(i) #output: 66.2

# type casting 

# int() function converts a number or string to an integer number.

k = 23
l = "23"
print(type(l))
m = int(l) # here m converts the value of str l to int and it store the int value as 23 
print(type(m))
print(k+m)#46


#input
name = input("Enter your name: ")
print("Hello, " + name + "!")
print("Lets Sum the two numbers")


num3 = input("enter the value first number : ")
num4 = input("enter the value second number : ")
print(type(num3))#str
print(type(num4))#str
print("The sum of two numbers is : ",int(num3)+int(num4)) # beacuse the num3 and num4 are strings thats why we type cast the value of numbers
#output: The sum of two numbers is : num3 + num4

# practice Question 
side = float(input("Enter the side of the square : "))
area = side * side
print("The area of the square is : ",area)
#output: The area of the square is : side * side