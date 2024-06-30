number= int(input("Enter a number to see its multiplication table: "))

for i in range(number):
    result= number*i
    print(f"{number} * {i} = {result}")