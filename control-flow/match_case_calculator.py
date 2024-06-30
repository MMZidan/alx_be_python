num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation =input("Choose the operation (+, -, *, /): ")


def operater(operation):
    match operation:
        case "+": print(f"The result is {num1+num2}")
        case "-": print(f"The result is {num1-num2}")
        case "*": print(f"The result is {num1*num2}")
        case "/": print(f"The result is {num1/num2}")
        case _: print("Please Enter operator from the specified above")

if operation=="/" and num2==0:
    print("Cannot divide by zero.")
else:
    operater(operation)