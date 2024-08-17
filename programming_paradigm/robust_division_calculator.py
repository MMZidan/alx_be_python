

def safe_divide(numerator, denominator):
    try:
        num1=float(numerator)
        num2=float(denominator)
        # print(type(numerator,denominator))
        return print(f"The result of the division is {num1/num2:.2f}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
