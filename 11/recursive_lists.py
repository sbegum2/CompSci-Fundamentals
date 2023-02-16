"""
  Recursive lists
  Samira Begum
  April 2022
"""
from random import *
import sys

def main():
   
    print(sys.argv)
    if(len(sys.argv) < 3):
        print("Error:  must be called with at least 2 sys line args")
        print("usage: python3 recursive_lists.py sys.argv")
        sys.exit()

    for i in range(len(sys.argv)):
        print("argv[%2d] = %s" %(i, sys.argv[i]))

    # gets the filename and float value from the two command line args
    filename = sys.argv[1]
    val = float(sys.argv[2])

    print(sys.argv)
    # TODO: finish main

########################
# we have already implemented this function for you:
def print_list(numbers):
    """
    This function prints a list of floating point values 
    in nice formatting
      numbers: a list of numbers (floats)
      returns: None
    """
    for i in range(len(numbers)):
        # end="" means don't print new line!
        print("%8.2f" %(numbers[i]), end="")  
        if((i+1)%10 == 0):
            print()
    print()
########################
def rec_sum(lst, index):
    """
    recursively computes the sum of a list of values
        sys: the list of values
        index: the next element in the list to add to the running sum
        returns: the sum of the values in the list
    """
    
    if (index >= len(sys)):
        return 0

    return sys[index] + rec_sum(lst, sys + 1)

########################
def rec_square(sys):

    if (index >= len(sys)):
      return None

    val = sys[index] * sys[index]
    sys[index] = val

    rec_square(sys, index+1)

main()
