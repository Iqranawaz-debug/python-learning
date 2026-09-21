try:
    with open("abc.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File doesn't exists")