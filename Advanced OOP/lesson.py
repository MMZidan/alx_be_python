class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
        
    def __del__(self):
        return "Farwell"
    def __str__(self):
        return f"{self.name} age is {self.age}"

class Human(Person):
    pass


MMZ=Human("MMZ",25)
print(MMZ)
#################################################
class Vehicle:
  def move(self):
    print("Moving...")

class Car(Vehicle):
  pass

class ElectricCar(Car):
  def charge(self):
    print("Charging...")

tesla = ElectricCar()
tesla.move()  # Output: Moving...
tesla.charge()  # Output: Charging...

#########################################################

class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass
obj_d = D()
print(A.greet)
print(obj_d.greet()) 

###########################################################
class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animals = [Dog(), Animal()]
for animal in animals:
  animal.make_sound() 

##########################################################

# class Duck:
#     def quack(self):
#         return "Duck quacks"

# class Person_1:
#     def quack(self):
#         return "Person imitates duck"

# person = Person_1()
# print(person.quack())

class Duck:
    def quack(self):
        return "Quack!"

class Dog:
    def quack(self):
        return "Bark!"

duck = Duck()
dog = Dog()

def make_sound(obj):
    return obj.quack()
print(make_sound(duck))  # Output: "Quack!"
print(make_sound(dog))   # Output: "Bark!"
############################################################

class shape:
   def __init__(self):
      pass

   
class rectangle(shape):
   def __init__(self, width, height):
        self.width = width
        self.height = height

   def calculate_area(self):
      return f"calculate rectangle area... {self.width*self.height}"
   
   def __repr__(self):
    return f"Area of Rectangle : {self.calculate_area()}"


rect= rectangle(5,10)

print(rect.calculate_area())
print(repr(rect))
###################################################################
class bird:
   def fly(self):
      print("Flying...")
class mammal:
   def run(self):
      print("Running...")
      return "Running . Running .."
   
class bat(bird,mammal):
   pass

animal = (bat())

animal.run()
animal.fly()
print(isinstance(animal,bird))
print(isinstance(animal,mammal))
##############################################################
import random
# Class Dog
class dog:
    @property
    def make_sound(self):
        return "Woof!"

# Class Cat
class Cat:
    @property
    def make_sound(self):
        return "Meow!"

# Class Bird
class Bird:
    @property
    def make_sound(self):
        return "Tweet!"    

def let_them_speak(animals):
    for animal in animals:
        animal=random.choice(animals)
        print(animal.make_sound)

ddog=dog()
Cat=Cat()
Bird=Bird()
animals = (ddog,Cat,Bird)
let_them_speak(animals)

###############################################################
class Book:
   total_books=0
   def __init__(self,name:str):
      self.name=name
      Book.total_books+=1
   @classmethod
   def display_total_books(cls):
      print(f"Total number of books {cls.total_books}")
   
   

Book1 = Book("Alice")
Book2 = Book("Bob")
book4 = Book("To Kill a Mockingbird")
book3 = Book("The Great Gatsby")

Book.display_total_books()
