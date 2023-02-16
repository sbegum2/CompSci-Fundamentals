"""
getnumbetween:

    Samira Begum
    February 2022
"""

def main():

    print(" ")
    result = getNumBetween(5, 13)
    print(" getNumBetween returned: " + str(result))
    print(" ")

def getNumBetween(low,high):

    user = int(input("Enter a value between 5 and 13: "))
    
    while(user < 5 or user > 13):
        print("hey! " + str(user) + " is not between 5 and 13 try again...")
        user = int(input("Enter a value between 5 and 13: "))

    else:
        return user

main()
