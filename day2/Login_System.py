correct_username = "Iqra"
correct_password = 1234
username = input("Enter username:")
password = int(input("Enter Password:"))
if username == correct_username and password == correct_password:
    print("Login Successful!")
else:
    print("Failure")