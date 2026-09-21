#adding content removing the previous one
with open("student.txt","w") as file:
    file.write("Iqra Nawaz\n")
    file.write("I'm a graduate\n")

#adding content and not removing the previous one
with open("student.txt","a") as file:
    file.write("Data Science")

with open("student.txt","r") as file:
    content=file.read()
print(content)
