#hello func
def hello():
    print("hello i'm learning python")
hello()
hello()

#greet func
def greet(name):
    print("Hello",name)
greet("Taiba")
greet("Laiba")

#even or odd func
def check_even(num):
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
check_even(3)
check_even(2)

#student details
def calculate_result(marks):
    average = sum(marks)/len(marks)
    print(average)
    if average >= 40:
        print("student is passed")
    else:
        print("Student failed")
    return marks

calculate_result([34,54,42])
calculate_result([34,30,43])