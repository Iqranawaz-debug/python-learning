class Student:
    def __init__(self,Roll_number,Name,Marks):
        self.Roll_number = Roll_number
        self.Name = Name
        self.Marks = Marks

Student1 = Student(12,"Iqra",90)
print(Student1.Name)
print(Student1.Roll_number)
print(Student1.Marks)
