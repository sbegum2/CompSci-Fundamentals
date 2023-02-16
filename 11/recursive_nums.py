"""
 Recursive functions
 Samira Begum
 April 2022
"""
from random import *

def main():

    print("\nFirst, try functions that compute the sum of the even numbers between 1 and n")
    n = (int(input("Enter a value for n: ")))
    lst = create_list(n)

    count = sum_of_evens_iter(lst)
    print("\nThe sum of the even numbers 1 to %d computed iteratively is %d" % (n, count)) 

    countR = sum_of_evens_recursive(n)
    print("The sum of the even numbers 1 to %d computed recursively is %d \n" % (n, countR))

    print("Next, let's try functions that sum a series")
    n = input("Enter the number of terms, n, in the series to sum: ")
    
    series = sum_series_iter(n)
    print("\nThe sum of the series for %d terms computed iteratively is %f" % (int(n), series))

    seriesR = sum_series_recursive(n)
    print("The sum of the series for %s terms computed recursively is %f \n" % (n, seriesR))

#############################################
def sum_of_evens_iter(lst):
    """
    Iteratively computes the sum of even values in the range of 1 through n
        n: integer user input
        returns: count(sum of even numbers)
    """ 
    count = 0
    for i in range(len(lst)):
        if ((lst[i] % 2) == 0):
            count += lst[i]
    return count

#############################################
def sum_of_evens_recursive(n):

    if n==0:
        return 0
    
    if((n % 2) == 0):
        part = sum_of_evens_recursive(n-1) 
        countR = n + part
        return countR
    else:
        part = sum_of_evens_recursive(n-1)
        countR = part
        return countR

#############################################
def sum_series_iter(n):

    ans = 0
    n = int(n)
    for i in range(1,n+1):
        val = float(1 / (2**i))
        ans = ans + val
    return ans
#############################################
def sum_series_recursive(n):

    seriesR = 0
    n = float(n)

    if n==0:
        return 0

    if n > 0:
        tester = float(1 / (2**n))
        part = sum_series_recursive(n-1)
        seriesR = tester + part
    else: 
        part = sum_series_recursive(n-1)
        seriesR = part
        return seriesR

    return seriesR

#############################################
def create_list(n):
    """
    Creates a list of numbers 1 through n
        n: number of elements
        returns: a list of n elements
    """

    lst = []
    for i in range(1,n+1):
        lst.append(i)
    
    return lst

#############################################

main()
