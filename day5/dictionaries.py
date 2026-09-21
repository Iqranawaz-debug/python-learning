student = {
    "name":"Iqra",
    "age":22,
    'cgpa':3.7,
     "id": 5
}
#add a new key
student["university"]="NED University"
print(student)

#remove a key
student.pop("age")
print(student)

#check if a key exists
if "name" in student:
    print("Name exists")

#loop through a dictionary
for key in student:
    print(key)
for value in student.values():
    print(value)
#both key and values
for key,value in student.items():
    print(key,":",value)