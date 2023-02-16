"""

Program to practice python math ops

Samira Begum
February 3, 2022

"""
    
def main():

    #prompt user to input integer values

    p = input("Enter a positive integer value: ")
    p = int(p)
    
    s = input("Enter another (small) positive integer value: ")
    s = int(s)

    #run all basic integer operations using user input
    #print integer ops

    print(p+s)
    print(p-s)
    print(p*s)
    print(p/s)
    print(p//s)
    print(p%s)
    print(p**s)

main()
