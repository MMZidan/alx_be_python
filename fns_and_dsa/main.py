from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation=='divide' and num2==0 :
        print("Can't divide by Zero")
    else: 
        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

# print(dir(calculator))
# x= float(input("Enter Value of X: "))
# y= float(input("Enter Value of Y: "))
# print(type(x))
# print(f"Add = {calculator.add(x,y)}")
# print(f"Subtract = {calculator.subtract(x,y)}")
# print(f"Multiply = {calculator.multiply(x,y)}")
# if y==0 :
#     print("Please Enter a valid number for Y (X/y)")
# else: 
#     print(f"Divide = {calculator.divide(x,y)}")