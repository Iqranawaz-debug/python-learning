import random
def check_guess():
    num=random.randint(1,5)
    guess = int(input("Enter your guess"))
    if num == guess:
        print("You guessed right")
    else:
        print("try again")
