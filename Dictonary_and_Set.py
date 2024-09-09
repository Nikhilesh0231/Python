#Dictionary
info = {
  "name":"Neelesh",
  "age":26,
  "city":"Manipur",
  "country":"India",
  "specialities":["C","Java","Python"]

}

print(info)
print(info["name"])
print(info["age"])
print(info["city"])
print(info["country"])
print(info["specialities"])

print(type(info))

info["surname"] = "Tiwrai"#We Can Add the keys 
print(info)

info["city"] = "Hyderabad"#we can modify the values of existing keys
print(info)

# if we try to add new key with same key name then the value of the key overites 
info["city"]="Mumbai"
print(info)

# And we can also create a null dictionary with no key values and later we can add the key values 

null_dict = {

}

print(null_dict)

null_dict["name"] = "Oxford"
print(null_dict)


#Nested Dictionary 
student = {
  "name":"Aman",
  "marks":{
    "maths":99,
    "chem":98,
    "phy":97
  }
}

print(student)
print(student["marks"]["maths"])
#Dictionay Methods
print(len(list(student.keys())))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"cgpa":9.8})
print(student)
new_dict = {
  "surname":"Kumar",
  "city":"Allahabad"
}
student.update(new_dict)
print(student)


# Set 

collection = {1,2,3,4,"hello","world"}
print(collection)
print(type(collection))
collection1 = { 1,1,1,2,2,3,4,5,5,"set","set"}
print(collection1)
print(len(collection1))
null_set = set()
print(null_set)
print(type(null_set))
null_set.add(4)
print(null_set)
null_set.add(2)
print(null_set)
null_set.add(6)
print(null_set)
null_set.add(7)
print(null_set)
null_set.remove(7)
print(null_set)
null_set.pop()
print(null_set)
null_set.clear()
print(null_set)


a = {1,2,3,4,5,6}
b ={4,5,6,7,8,9}
# Union of two sets
print(a.union(b))
# Intersection of two sets
print(a.intersection(b))