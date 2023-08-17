# Temperature Converting Program 

def convert_temperature():
    print("--------------------------------")
    print("Welcome to Temperature Converter")
    print("--------------------------------")
    Temp_unit = int(input("Select the Temperature Unit\n1. Celsius\n2. Fahrenheit\n3. Kelvin\nEnter your choice: "))
    Temp_amount = float(input("Enter the amount of Temperature to convert: "))

    print("--------------------------------")
    print("            Results             ")
    print("--------------------------------")

    if Temp_unit == 1:
        print(f"{Temp_amount} Celsius in Fahrenheit = ", round(1.8 * Temp_amount + 32, 2))
        print(f"{Temp_amount} Celsius in Kelvin = ", round(Temp_amount + 273.15, 2))
    elif Temp_unit == 2:
        print(f"{Temp_amount} Fahrenheit in Celsius = ", round((Temp_amount - 32) / 1.8, 2))
        print(f"{Temp_amount} Fahrenheit in Kelvin = ", round((Temp_amount - 32) / 1.8 + 273.15, 2))
    elif Temp_unit == 3:
        print(f"{Temp_amount} Kelvin in Celsius = ", round(Temp_amount - 273.15, 2))
        print(f"{Temp_amount} Kelvin in Fahrenheit = ", round((Temp_amount - 273.15) * 9/5 + 32, 2))
    else:
        print("Invalid Input (Enter 1 or 2 or 3)")

Proceed = True

while Proceed == True:
    convert_temperature()
    print("--------------------------------")
    print("Do you want to convert again?")
    print("Press 1 to convert again")
    print("Press 2 to exit")
    Proceed = int(input("Enter your choice: "))
    if Proceed == 1:
        Proceed = True
        print("Let's convert again")
    elif Proceed == 2:
        Proceed = False
        print("Thank you for using this program")
        print("Created By: Wakil Ahmad Hamidi")
    else:
        print("Invalid Input")
        break

convert_temperature()
