"""
A program that converts a user-given Fahrenheit temperature to Celsius

Samira Begum
February 2022

"""

def main():
    
    print("Hello! We're going to convert degrees Fahrenheit to Celsius")
    F = input("Enter the temperature in degrees F: ")
    F = float(F)

    C = ((F-32)*(5/9))
    C = str(C)
    F = str(F)

    print(F + " degrees Fahrenheit converted to Celsius is " + C)

main()
