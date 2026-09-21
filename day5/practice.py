#dictionary
student={
    "name":"iqra",
    "age":22,
    "university":"NED Uni",
    "CGPA":3.7
}
print(student["name"])
print(student["age"])
print(student["university"])
student["CGPA"]=3.8
student["skills"]="Python"
student.pop("age")
print(student)

#tuple
tuple = ("Iqra",22,"NED Uni")
print(tuple[0])

#convert into set and print unique numbers
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
num_set = set(numbers)
print(num_set)

#loop in dictionary
student = {
    "name": "Iqra",
    "Python": 85,
    "SQL": 78,
    "Power BI": 90
}
for key,value in student.items():
    print(key,":","value")

