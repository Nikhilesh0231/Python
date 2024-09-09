# f = open("demo.txt","r")
# # data = f.read()#It reads the entire file 
# # data = f.read(5)#it read first five characters of the page#for this type of data is string
# data = f.readline()#by this we can read line by line
# print(data)
# print(type(data))



# f = open("demo.txt","w")
# data = f.write("this is going to be my new line in the file and the previous string will be overwrites")
# print(data)
# print(type(data))


# with syntax

# with open("demo.txt","r") as f :
#   data = f.read()
#   print(data)

# with open("demo.txt","w") as f :
#   data = f.write("hello")

  
# with open("demo.txt","r") as f :
#   data = f.read()
#   print(data)

# deleting file 
import os 
os.remove("demo.txt")