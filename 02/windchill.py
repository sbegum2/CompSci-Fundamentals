"""
A program that converts a user-given temperature and windspeed to degrees Celsius and Fahrenheit

Samira Begum
February 2022

"""

def main():
    
    print("This program computes wind chill in Fahrenheit and Celsius")
    F = input("Enter the current temperature (in F): ")
    WV = input("Enter the wind velocity (in miles/hr): ")

    F = float(F)
    WV = float(WV)

    WC = (35.74 + (0.6215*F) - (35.75*(WV**0.16)) + (0.4275 * F * (WV**0.16)))
    
    F = str(F)
    WV = str(WV)

    C = ((WC-32)*(5/9))
    WC = str(WC)
    C = str(C)

    print()
    print("When the temperature is " + F + " and wind speed is: " + WV)
    print("  the wind chill in F is " + WC)
    print("  the wind chill in C is " + C)

main()
