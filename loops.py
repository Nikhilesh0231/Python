count = 1
while count <= 5 : 
  print("hello")
  count = count +1;
print(count)


i = 1
while i <= 4 :
  print("This is Nikhilesh ",i)
  i += 1

  #print numbers 1 to 50

  i = 1
  while i < 51 :
    print(i)
    i += 1

#Question --> Print numbers from 1 to 100

i = 1
while i<=100:
  print(i)
  i+=1

#Question --> Print numbers from 100 to 1

i = 100
while i >= 1:
 print(i)
 i-=1

#question : print the multiplication table of a number n  \

n = int(input("Enter a number : "))
i = 1
while i <= 10 :
  print(n,"*",i,"=",i*n )
  i+=1

#Question --> print the elements of the following list using a loop 

list = [1,4,9,16,25,36,49,64,81,100]
print(len(list))
i = 1
while i < len(list):
  print("Element at Index ",i-1,":",list[i-1])
  i+=1
  
#Question --> Search for a number x in this tuple using

tuple = (1,4,9,16,25,36,49,64,81,100)
a = int(input("Enter a number to be search : "))
i = 1
while i < len(tuple):
  if a == tuple[i]:
    print("Number Found")
    break
  i+=1
else:
  print("Number Not Found")
#break and continue in loop  
j = 1
while j <= 5:
  print(j)
  if j==3:
    break  #it stops the further execution 
  j+=1
k = 1
while k <= 5:
  if (k==3):
    k+=1
    continue  #it skips the condition
  print(k)
  k+=1

  #Question tpo print odd numbers from to 1 to 50

num = 1
while num <=50:
  if(num%2 == 0):
     num+=1
     continue
  print("Odd Number",num)
  num+=1

  #Question tpo print even numbers from to 1 to 50

num = 1
while num <=50:
  if(num%2 != 0):
     num+=1
     continue
  print("Even Number",num)
  num+=1

# for Loops 

listFruits = ["apple","banana","orange","grapes","watermelon","Mango","Muskmelon","kiwi","litchi","jackFruit"] 

for fruit in listFruits:
  print(fruit)

tupVeggies = ("potato","tomato","onion","garlic","ginger","capsicum")
for vegi in tupVeggies:
  print(vegi)
#forloop with else
str = "Thisloopisquitegood"
for char in str:
  print(char)
else:
  print("This is all about loops.")


#range() 
seq= range(5)
print(seq[1])

for el in range(6):
  print(el)#0,1,2,3,4,5

for el in range(1,6):
  print(el)#1,2,3,4,5

for el in range(1,6,2):
  print(el)#1,3,5
#Print numbers from 100 to 1
for num in range(100,0,-1):
  print(num)

#print the table for a n number

tab = int(input("Enter a number : "))

for i in range (1,11):
  print(tab,"*",i,"=",tab*i)

#pass statement 
# # use of pass statement
# for l in range(5):
#   #empty
# print("some useful work")# here we can not achieve it so for achieb=ving it can do the same with pass statement

for l in range(5):
  pass
print("some useful work")


#Write a program to find the sum of first n natuaral numbers 

inum = int(input("Enter a number to get the sum at that number:"))
sum = 0
i = 1
while i <= inum :
  sum = sum+i
  i+=1
print(sum)

inum2 = int(input("Enter a number to get the sum at that number:"))
sum = 0
for i in range(1,inum2+1):
  sum+=i
print("total sum is",sum)


#Write a program to find factorial of n number
fnum = int(input("Enter a number to get the factorial of at that number:"))
f=1
for i in range(1,fnum+1):
  f*=i
print("The factorial is -",f)

fnum2 = int(input("Enter a number to get the factorial of at that number:"))
f=1
i =1
while i <=fnum2:
  f*=i
  i+=1
print("Factorial = ",f)
