#################function###############################
def calcSum(num1,num2):#here a and b is parameter 
  sum =  num1 + num2
  return (print("The sum of",num1,"and",num2,"is :",sum))#function definition

calcSum(2,3)#function call#here the value we passed is known as argument

def print_hello():
  return "hello"

print(print_hello())
#creating a function which calculates average of three numbers 

def calc_avg(n1,n2,n3):
  avg = (n1+n2+n3)/3
  return print("The average of Numbers is :",avg)

calc_avg(2,4,6)


def calc_Prod(a=1,b=1):
  product = a * b
  return print("The product of",a,"and",b,"is :",product)
calc_Prod()#1 as it take both default values 
calc_Prod(2)#2 it 2 as argument for a and for b it uses default value
calc_Prod(2,3)#6 it 2 and 3 as value of a and b


#practice Questions 
#1. Write a function to print the length of a list (list is parmeter)
def len_list(list):
  return print("The length of list is :",len(list))

len_list([1,2,3,4,5,6,7,8])
#2. Write a function to print the element of a list in a single line.
def print_list(list):
  for l in list:
    print(l,end=" ")
  
print_list([1,2,3,4,5,6,7,8])
print()
#3. Write a function to find the factorial of n .(n as parameter)

def calc_factorial(n):
  fact = 1
  for i in range(1,n+1):
    fact = fact * i
  return print("The factorial of",n,"is :",fact)

calc_factorial(5)

#4. Write a function to convert USD to INR

def curr_con(dol):
  inr = dol * 83.88
  return print("The value of",dol,"USD is :",inr,"INR")

curr_con(100)

###############################RECURSION#######################################
#suppose we want to print 5,4,3,2,1 in single call

def show(n):
  if (n==0):
    return 
  print(n)
  show(n-1)
  
show(5)

#Calculate factorial using recursion

def fact(n):
  if (n == 0):
    return 1
  return n * fact(n-1)

resfact = fact(5)
print(resfact)


#Practice Question
#1. Write a function to find the sum of first n natural numbers using recursion

def cal_sum_n(n):
  if (n == 0):
    return 0
  return n + cal_sum_n(n-1)

res_sum = cal_sum_n(10)
print(res_sum)

#2. write a recrssive function to print all elements in a list 

def print_flist(list,idx=0):
  if (idx == len(list)):
    return
  print(list[idx])
  print_flist(list,idx+1)

listFruits = ["apple","banana","orange","grapes","watermelon","Mango","Muskmelon","kiwi","litchi","jackFruit"] 
print_flist(listFruits)
    