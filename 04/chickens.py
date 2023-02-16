"""
  Program to convert egg weight to egg size

  Samira Begum
  February 2022
"""

def main():

    print(" ")
    print("Welcome to the chicken egg sizing program")
    weight = float(input("Enter the weight of the chicken egg in grams: "))
    print(" ")


    if(weight >= 71):
        print("This is a jumbo egg.")

    elif(weight >= 64):
        print("This is an extra large egg.")

    elif(weight >= 57):
        print("This is a large egg.")

    elif(weight >= 50):
        print("This is a medium egg.")

    elif(weight >= 43):
        print("This is a small egg.")

    elif(weight >= 35):
        print("This is a peewee egg.")

    else:
        print("This egg is too small to grade.")

main()
