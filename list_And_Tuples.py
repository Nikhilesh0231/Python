marks = [22,23,12,43,45,56,76,67]
print(marks)
print(type(marks))

print("Marks at index 0 : ",marks[0])
marks[0] = 99
print("Marks at index 0 : ",marks[0])

print("Marks at index 1 : ",marks[1])
print("Marks at index 2 : ",marks[2])
print("Marks at index 3 : ",marks[3])
print("Marks at index 4 : ",marks[4])
print("Marks at index 5 : ",marks[5])
print("Marks at index 6 : ",marks[6])
print("Marks at index 7 : ",marks[7])

student =["Nikhil",23,"Delhi","MCA","Working"]
print(student)
print(student[3])

print("The length of Student list is : ",len(student))
print("The lenght of marks list is : ",len(marks))

#Slicing In List 

StuMarks = [67,89,87,76,65,54]

print(StuMarks[1:3])#89,87
print(StuMarks[1:5])#89,87,76,65
print(StuMarks[:4])#67,89,87,76
print(StuMarks[1:])#89,87,76,65,54
print(StuMarks[-6:-3])#67,89,87

#List methods 

list = [2,1,3]
list.append(4)
print(list) #[2,1,3,4]
list.sort()
print(list) #[1,2,3,4]
list.sort(reverse=True)
print(list) #[4,3,2,1]


list1 = [2,4,7,8,9,6]
list1.reverse()
print(list1) #[6,9,8,7,4,2]

list.insert(0,5)
print(list) #[5,4,3,2,1]

list2 = [2,1,3,1]
list2.remove(1)
print(list2) #[2,3,1]

list2.pop(2)
print(list2) #[2,3]

#Tuples
tup =  (1,4,2,3)
print(type(tup))
print("Value at index 0 : ",tup[0])
print("Value at index 1 : ",tup[1])
print("Value at index 2 : ",tup[2])
print("Value at index 3 : ",tup[3])
# print("Value at index 4 : ",tup[4])#IndexError: tuple index
tup1=()
print(tup1)
tup2 = (1)#it will not consider as tuple 
print(type(tup2))#<class 'int'>
# the correct way to store a single value in tuple is
tup3 = (1,)#it will consider as tuple
print(type(tup3))#<class 'tuple'>

#Slicing in tuples 
tup4 = (1,2,4,6,8,9)
print(tup4[0:3])#(1,2,4)

#Tuple Methods 
tupl = (2,3,4,5,1,2,3,2,4)

print(tupl.index(5))#output: 3
print(tupl.count(2))#output: 3


#Question --> Write a program to ask the user to enter names of their three favourite movies & Store them in a list
mov1 = input("Enter the name of first favourite movie of yours :- ")
mov2 = input("Enter the name of second favourite movie of yours :- ")
mov3 = input("Enter the name of third favourite movie of yours :- ")

movlist = []
movlist.append(mov1)
movlist.append(mov2)
movlist.append(mov3)
print("The list of Your Favourite movies is = ",movlist) #[input1,input2,input3]

#Write a Program to check if a list contains a palindrome of elements.
plist1 = [1,2,3,2,1]

copy_plist1 = plist1.copy()#it gives the copy of the list 

copy_plist1.reverse()

if copy_plist1 == plist1 :
  print("The list is a palindrome list",plist1)
else:
  print("The list is not a palindrome list",plist1)#The list is not a palindrome


plist2 = [1,2,3]

copy_plist2 = plist2.copy()#it gives the copy of the list 

copy_plist2.reverse()

if copy_plist2 == plist2 :
  print("The list is a palindrome list",plist2)
else:
  print("The list is not a palindrome list",plist2)#The list is not a palindrome

#write a program to count the number of students with grade "A" in the folowing tuple
#("A","B","C","D","A","B","A","C")

Grades = ("A","B","C","D","A","B","A","C")
print(Grades.count("A"))

#Store the values in the list and sort them from Ato D
Grades = ["A","B","C","D","A","B","A","C"]
Grades.sort()
print(Grades) #[A, A, A, B, B, C, C,
