#Strings
str1 = 'Python'
str2 = "is best"
str3 = """programming Language."""
print(str1,str2,str3) 

print(str1 + "    " + str2)#we can add spaces also in the line


str = "This Progrmming gives a lot of \n of freedom to write the code in simpler way"
print(str)

a = "ABCDEFGHIJKLMN"
b = "OPQRSTUVWXYZ"
print(a+b)#Conatenation

word = "Comment"
c=len(word)
print(c) #Length of the string if spaces are in the then apces also count in the length of the string   

ch = word[0]
print(ch) #First character of the string
ch1 = word[4]
print(ch1) #5th character of the string
#Slicing
str4 = "NumericalAnalysis"
print(len(str4))

print(str4[2:8])
print(str4[9:12])
print(str4[ :4])
print(str4[10:])

# Slicing Over Negative Index

fruit = "Apple"
print(fruit[-3 : -1])
# StringFunction
str5 = "i am a Coder.";
print(str5.capitalize()) # Capitalize the first letter of the string
print(str5.casefold()) # Convert the string to lowercase
print(str5.endswith("er."))# Check if the string ends with the specified value
print(str5.find("Coder")) # Find the index of the first occurrence of the specified value
print(str5.replace("Coder" , "Doctor"))#Relaces all occurrences of old with new
print(str5.count("am"))#Count the occurrences of substring in string



#Conditional Statement 

#if-elif-else

age = int(input("Enter Your Age : "))
if 18 <= age <= 60:
  print("You can apply for driving license")
elif age > 60:
  print("You are not eligible for driving license!!! . You are to old")
else:
  print("You are kid")

light = "green"
if light == "green":
  print("Go")
elif light == "red":
  print("Stop")
else:
  print("Wait")


#Grade Students according to their marks 

marks = int(input("Enter Your Marks : "))

if marks >= 90 :
  print("Grade A")
elif 90 > marks >= 80:
  print("Grade B")
elif 80 > marks >= 70 :
  print("Grade C")
elif 70 > marks >= 60 :
  print("Grade D")
elif 60 > marks >= 50 :
  print("Grade E")
else:
  print("Grade F "+"You are fail")

#nesting

YourAge = int(input("Enter Your Age : "))

if YourAge >= 18:
  if YourAge >= 80:
    print("You are old "+"You Cannot Drive")
  else:
    print("You are adult " + "you can drive")
else:
  print("You are kid "+"You cannot drive")

  #question 

#Write a Program to check whether the given number is odd or even 
number = int(input("Enter your Number : "))

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# write a program to find the greatest of three numbers entered by the user 

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
if num1 > num2 and num1 > num3:
  print("The greatest number is : ", num1)
elif num2 > num1 and num2 > num3:
  print("The greatest number is : ", num2)
else:
  print("The greatest number is : ", num3)

#Write a program to check if number is multiple of 7 or not.

num  = int(input("Enter the Number : "))
if num % 7 == 0 : 
  print("The number is multiple of 7")
else :
  print("The number is not multiple of 7")