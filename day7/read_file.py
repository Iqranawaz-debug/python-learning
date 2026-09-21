#reading a file in python
file = open("student.txt","r")
content = file.read()
print(content)
file.close()

#another method to read a file
with open("student.txt","r") as file:
    content=file.read()
print(content)

#reading line by line
with open("student.txt","r") as file:
    for line in file:
        print(line.strip())