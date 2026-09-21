with open("names.txt","r") as file:
    for line in file:
        print(line.strip())

with open("skills.txt","w") as file:
    file.write("Python\n")
    file.write("SQL\n")
    file.write("PowerBI\n")
    file.write("Git\n")
with open("skills.txt","a") as file:
    file.write("Data engineering")