# object = A bundle of related attributes and methods
#examples : phone , cup and book 

#class = blueprint used to design the structure and layout
class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale=for_sale

    def drive(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

car1 = Car("Mustang",2024,"black",False)
print(car1.model)
print(car1.year)
print(car1.color)

car1.stop()

