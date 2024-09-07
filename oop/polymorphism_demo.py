import math
class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    # @property
    def area(self):
        return f"The area of the Rectangle is: {self.length*self.width}"
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    # @property
    def area(self):
        area = math.pi * (self.radius ** 2)
        return f"The area of the Circle is: {area}"
    


# def main():
#     shapes = [
#         Rectangle(10, 5),
#         Circle(7)
#     ]

#     for shape in shapes:
#         print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

# if __name__ == "__main__":
#     main()
