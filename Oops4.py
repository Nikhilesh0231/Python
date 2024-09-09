class Person:
  name = "Anonymous"
  # def ChangeName(self,name):
    # self.name = name
    # Person.name = name
    # self.__class__.name = name
  @classmethod
  def ChangeName(cls,name):
    cls.name = name

p1 = Person()
print(p1.name)
p1.ChangeName("Nikhilesh")
print(p1.name)
print(Person.name)


class Student:
  def __init__(self,phy,chem,math):
    self.phy =phy
    self.chem = chem
    self.math = math
    # self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
  @property
  def percentage(self):
    return str((self.phy+self.chem+self.math)/3)+"%"
stude1 = Student(98,23,21)
print(stude1.percentage)

stude1.math = 96
print(stude1.math)
print(stude1.percentage)
