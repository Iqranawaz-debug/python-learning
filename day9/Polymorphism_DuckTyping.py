class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    is_alive = False
    def speak(self):
        print("HONK")

Animals = [Dog(),Cat(),Car()]
for animal in Animals:
    print(animal.is_alive)