# class Student:
#   name="Ripunjay"

# s1 = Student()
# print(s1.name)

class Car :
  color = "black"
  brand = "Mahindra"
  model = "Scorpio"

car1 = Car()
print(car1.color)
print(car1.brand)
print(car1.model)

class Student:

  name = "Anonymous"#Class Attribute 
  #default constructor
  def __init__(self):
    print("I am default constructor")

    #parametrized constructor
  def __init__(self,fullname,marks) :
    self.name = fullname#Object Attribute >> precidence over class Attribute
    self.marks = marks
    print("Adding new student in database..")

s1 = Student("Shukla",990)
print(s1.name)
print(s1.marks)

s2 = Student("Ashrut Shukla",9000)
print(s2.name)
print(s2.marks)

print(Student.name)


class Teacher :
  def __init__(self, name):
    self.name = name 
  def hello(self):
    print("Hello, my name is", self.name)

t1 = Teacher("Nikhilesh Tiwari")
print(t1.name)
t1.hello()


#Create student class that takes name and marks of three Subjects as argument in constructor .
#then create a method to print the average
   

class student :
  @staticmethod
  def hello():
    print("Hello, I am a student")
  def __init__(self, name, marks1, marks2, marks3):
    self.name = name
    self.marks1 = marks1
    self.marks2 = marks2
    self.marks3 = marks3
  def average(self):
    return (self.marks1 + self.marks2 + self.marks3)/3
  
student1 = student("Ashrut",99,98,98)

print(student1.name)
print(student1.marks1)
print(student1.marks2)
print(student1.marks3)

print(student1.average())
student1.hello()
student.hello()

