import unittest

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def read_student(self):
        return print(f"{self.name} is a student, Age is {self.age}")

class product:
    instances = []
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        product.instances.append(self)


    def total_stock(self):
        return self.price*self.quantity

def divide_numbers():
    num1 = float(input("Enter the first number (numerator): "))
    num2 = float(input("Enter the second number (denominator): "))
            
            # Perform the division
    try:
            result = num1 / num2
    except ZeroDivisionError:
            print("Cannot divide by Zero")    
            # raise ZeroDivisionError
            # Display the result
    else:
            print(f"{num1} divided by {num2} is: {result:.2f}")

def open_file():
    try:
        f= open('test.py')
    except FileNotFoundError as e:
        #  print("file not found")
        print(e)


def custom_exception():
    num = float(input("Enter the number : "))
    try:
         if num>=100:
              raise Exception 
    except Exception :
         print("ValueTooHighError")

student1=student("Mike","29")
product2 = product("Banana", 0.25, 50)
product3 = product("Orange", 0.75, 75)
product1 = product("Apple", 0.5, 100)


if __name__ == "__main__":
    # unittest.main()
    student1.read_student()
    # total_price=0
    # for product in product.instances:
    #     product.price=float(product.price)
    #     total_price+=product.price
    total_price = sum(product.price for product in product.instances)
    print(total_price)
    divide_numbers()    
    open_file()
    custom_exception()