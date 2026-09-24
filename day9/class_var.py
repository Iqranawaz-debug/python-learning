#A class variable is one value that is shared by all objects of a class.
class Student:
    class_year = 2026
    num_student = 0
    def __init__(self , name ,roll_num , age):
        self.name = name
        self.roll_num = roll_num
        self.age = age
        Student.num_student +=1


    def take_quiz(self):
        print("Take quiz")

    def check_copy(self):
        print("Get your copy checked")

student1= Student("Iqra",5,23)
student2 = Student("Laiba",6,24)
student3=Student("Sameen",7,23)
print(Student.class_year) #access directly from class,not any instance
print(f"Our graduating class of batch {Student.class_year} has {Student.num_student} students")