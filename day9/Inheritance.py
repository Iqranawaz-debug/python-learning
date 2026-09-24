#Inheritance = ALlows a class to inherit attributes and methods from another class
#helps in reusability and extensibility
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name}is eating")

    def sleep(self):
        print(f"{self.name}is sleeping")

class Dog(Animal):
    def Speak(self):
        print("WOOF")
class Cat(Animal):
    def Speak(self):
        print("MEOW")

class Mouse(Animal):
    def Speak(self):
        print("SQUEEK")

dog = Dog("Scobby")
cat = Cat("Tom")
mouse = Mouse("Jerry")
dog.Speak()
cat.Speak()
mouse.Speak()