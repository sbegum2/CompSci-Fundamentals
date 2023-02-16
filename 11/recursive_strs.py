"""
 Recursive strings
 Samira Begum
 April 2022
"""
from functools import partialmethod
from random import *

def main():
    print("\nThis program counts the number of lower case alpha characters in a string.")
    string = (input("Enter a string value: "))

    while not(string.isalpha()):
        print("\nHey that's not a string!")
        string = (input("Enter a string value: "))

    print("\nThe number of lower case characters in the string %s" % (string))
   
    lower = count_lower_iterative(string)
    print("\n   is %d computed iteratively" % (lower))

    lowerR = count_lower_recursive(string)
    print("   is %d computed recursively" % (lowerR))

def count_lower_iterative(string):

    lower = 0
    for i in range(len(string)):
        if string[i].islower():
            lower = lower + 1

    return lower

def count_lower_recursive(string):
    
    if string == "":
        return 0

    if string[0].islower():
        part = count_lower_recursive(string[1:])
        lowerR = 1 + part
        return lowerR
    
    else:
        part = count_lower_recursive(string[1:])
        lowerR = part
        return lowerR
            
main()