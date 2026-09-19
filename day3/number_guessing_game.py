secret_number=7
count=1
for i in range(1,20):
    num=int(input("Guess the number:"))
    if num ==secret_number:
        print("You guessed it right!")
        break
    elif num>secret_number:
        print("Higher")
    elif num<secret_number:
        print("Lower")