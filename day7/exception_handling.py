#zero division error(1/0) , value error(int("pizza")) and type error(1+"1")
try:
    num = int(input("Enter a number:"))
    print(1/num)
except ZeroDivisionError:
    print("Enter a number other then zero")
except ValueError:
    print("Enter a number please")
except TypeError:
    print("not compatible")