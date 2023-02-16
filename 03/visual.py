"""
Program that uses dots to visualize viral spread

Samira Begum
February 2022
"""

def main():
    R = float(input("What's the R value? "))
    C = int(input ("How many cycles? "))

    for i in range(C+1):
        start = (float(R**(i-1)))
        print("." * (int(start*R)))
        print(" ")

main()
