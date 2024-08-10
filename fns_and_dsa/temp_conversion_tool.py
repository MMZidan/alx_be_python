FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(Temp):
    Temp_final= (Temp-32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{Temp}°F is {Temp_final}°C")

def convert_to_fahrenheit(Temp):
    Temp_final= (Temp+32)*CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{Temp}°C is {Temp_final}°F")

if __name__ == "__main__":
    while True:
        try:
            Temp = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

            if unit=="c":
                convert_to_fahrenheit(Temp)
            elif unit=="f":
                convert_to_celsius(Temp)
            else:
                print("Invalid temperature. Please enter a numeric value.")

        except:
            print("Invalid temperature. Please enter a numeric value.")
    
        another = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break