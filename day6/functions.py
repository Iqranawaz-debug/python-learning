#average function
def calculate_average(marks):
    return sum(marks)/len(marks)

marks1=[34,67,56,55]
print(calculate_average(marks1))

marks2=[34,43,23,11]
print(calculate_average(marks2))

#hello function
def say_hello(name):
    print("Hello",name)
say_hello("Iqra")
say_hello("Hina")
say_hello("Fatima")

#add function
def add(a,b):
    print(a+b)
add(1,3)
add(3,4)

#return statement
def add(a,b,c):
    return a+b+c
result = add(1,4,5)
if result>9:
    print("You got bigger number")
