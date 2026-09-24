#Multi level inheritance = C(B) <- B(A) <- A
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"The {self.name} can eat")
    def sleep(self):
        print(f"The {self.name} can sleep")
class Prey(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey , Predator):
    pass

rabbit = Rabbit("Heroku")

rabbit.eat()