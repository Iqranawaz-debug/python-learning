#when we want to use the parent's method while also adding something of your own.
class Shape:
    def __init__(self ,color ,is_filled):
        self.color = color
        self.is_filled = is_filled
class Triangle(Shape):
    def __init__(self , color , is_filled ,length , width):
        super().__init__(color,is_filled)
        self.length = length
        self.width = width
class Circle(Shape):
    def __init__(self,color , is_filled ,radius):
        super().__init__(color,is_filled)
        self.radius = radius
class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

triangle = Triangle("Red",True,4,3)
circle = Circle("Blue",False,3)
square = Square("Yellow",True,4)

