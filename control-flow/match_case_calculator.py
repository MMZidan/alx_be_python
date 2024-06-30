num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator =input("Choose the operation (+, -, *, /): ")
if operator== "+":
    result = num1+num2
    print(f"The result is {result}")
elif operator=="-":
    result = num1-num2
    print(f"The result is {result}")
elif operator=="*":
    result= num1*num2
    print(f"The result is {result}")
elif operator=="/":
    match num2:
        case 0: print("Cannot divide by zero.")
        case _: print(f"The result is {num1/num2}")
    