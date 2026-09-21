import string
try:
    name = input("Enter name:")
    age = int(input("Enter age:"))
    CGPA = float(input("Enter CGPA:"))
    with open("student.txt","w") as file:
        file.write(name)
        file.write("\n")
        file.write(str(age))
        file.write(str(CGPA))
except FileNotFoundError:
    print("File doesn't exists")
except ArithmeticError:
    print("arithmetic error")
except BytesWarning:
    print("Byte warning")
except ValueError:
    print("Value error encountered")