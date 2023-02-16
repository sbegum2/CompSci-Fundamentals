"""
 TDD for search-dams.py

 Samira Begum
 April 2022
"""

from hydrodam_lab import *

def main():

 # 1. run getInput()
 # 2. while loop keeps running getInput() and running search when not quit 

--------------------------
def readData():
 """
 function to open, read, and close data file
   parameters: None
   returns: None
 """

 # 1. open CORGIS (small)
 
 # 3. close CORGIS (small)

--------------------------
def getInput():
 """
 function to get search parameters and search type
   parameters: None
   returns: search type of binary or linear
 """


 # 1. get user input for the option of searching by name(1) or state(2)
 #   a) implement quit option(3)
 #     i) break statement
 #   b) account for invalid input (alphabet, not 1 2 or 3, etc)
 
 # 2. if statement that gets input for linear or binary search on chosen var
 #   a) exit program option(3)
 #     i) break statement
 #   b) account for invalid input
 #   c) return search type as linear or binary

--------------------------
def linearSearch(search):   
 """
 function to get a search term and run linear search on it
   parameters: search - linear search type
   returns: search term
 """
    
 # 1. get user input for search term
 #  a) account for invalid input (not in data set)

 # 2. run linear search
 #  a) accumulate a list of matching search results

 # 3. return result list

--------------------------
def binarySearch(search):
 """
 function to get a search term and run binary search on it
   parameters: search - binary search type
   returns: search term
 """

 # 1. get user input for search term
 #  a) account for invalid input (not in data set)
 
 # 2. run binary search
 #  a) call lookForwardBackward() twice
 #  b) searches for partial match if searching by dam name

 # 3. return result

--------------------------
def printSearch(result):
 """
 helper function to print out tabular results of user's search term
   parameters: result - object to print
   returns: None
 """

 # 1. print formatted search results

--------------------------

main()
