try:
    for i in range(0,3):
        name=input("Enter your name:")
        marks=int(input("Enter your marks:"))
        with open("student.txt","a") as file:
                file.write(name)
                file.write("\n")
                file.write(str(marks))
                file.write("\n")

except FileNotFoundError:
    print("file doesn't exists")

except ValueError:
    print("Enter correct format")


