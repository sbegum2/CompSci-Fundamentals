"""
 Search dams
 Samira Begum
 April 2022
"""

from hydrodam_lab import *

def main():

    printIntro()
    data = readData()
    var = getInput()

    myDam = []
    for i in range(len(data)):
        x = data[i].split(",")
        myDam.append(HydroDam(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    while var != 3:
        var == False
        search = searchType(var)
        find = searchInput(var)
        find = find.capitalize()

        if search == 'quit':
            lst = []
            printInvalid(lst, search)
            print("\n Goodbye! \n")
            break
    
        elif search == 'linear' or search == 'binary':
            lst = searching(search, myDam, find)
            printInvalid(lst,search)
            if len(lst) > 0:
                print()
                printSearch(lst)
        var = getInput()

def printIntro():

    print("\n This program searches for dam names and U.S. states in a dataset. \n Tabular results are best displayed in a minimum terminal window width of 100.")

def readData():
    """
    function to open, read, and close data file
      
      parameters: None
      returns: data - list of info from file
    """
    
    file_name = "/data/cs21/hydropower/hydropower.csv"
    files = open(file_name, "r")
    data = files.readlines()
    files.close()

    for i in range(len(data)):
        data[i] = data[i].strip()
 
    return data


def getInput():
    """
    function to recieve user input on what data variable to search for 
      or to quit
      
      parameters: None
      returns: var - determines what variable to search by (dam name or state)
    """
    
    valid = False
    while valid == False:
        print("\n \n Please select 1, 2, or 3 from the menu below")
        search_info = input("\n 1. Search by dam name \n 2. Search by dam location (state) \n 3. Quit \n \n Choice? ")
        if search_info == '1' or search_info == '2' or search_info == '3':
            valid = True

    var = search_info

    return var

def searchType(var):
    """
    function to get search type
      
      parameters: var - determines what variable to search by (dam name or 
        state)
      returns: search - search type of binary or linear or none(quit)
    """
    
    if var == '1':
        valid = True
        search = 'binary'
        return search
  
    elif var == '2':
        valid = True

        search = 'linear'
        return search
    
    elif var == '3':
        valid = False
        search = 'quit'
        return search
        #print("\n Goodbye!")

def searchInput(var):
    """
    function to get user input on what term to search for in dataset
      
      parameters: var - variable to search for
      returns: find - search term
    """

    if var == '1':
        print()
        find = input(" Dam name (or prefix)? ")

    elif var == '2':
        print()
        find = input(" Location (state)? ")

    elif var == '3':
        find = "None"

    return find

def searching(search, myDam, find):
    """
    function to run linear search when looking for a state, run binary
      search when searching for a Dam name where the matching middle index is
      found and is searched left of and right of the middle index, and append 
      all found indices of the search term to a list (lst)
      
      parameters: search - search type of binary or linear or none(quit),
        myDam - split list version of dataset, find - search term
      returns: lst - list of dataset indices where search term (find) 
        was found
    """

    if search == 'linear':
        lst = []
        for i in range(len(myDam)):
            if myDam[i].get_state() == find:
                lst.append(myDam[i])

    if search == 'binary':
        lst = []       
        low = 0
        high = len(myDam) - 1
        while (low < high):
            mid = (low+high) // 2
            if myDam[mid].get_name().startswith(find):
                lst += (lookForwardBackward(myDam,mid,find,1))
                lst.append(myDam[mid])
                lst += lookForwardBackward(myDam,mid,find,-1)

                break

            elif find < myDam[mid].get_name():
                high = mid - 1
            else:
                low = mid + 1

    return lst

def printSearch(lst):
    """
    helper function to print out tabular results of user's search term
      
      parameters: lst - list of indices where search term (find) was found
      returns: None
    """
    print()

    print("%11s Dam Name %8s Watercourse %8s County %7s State %3sHeight%3sLength%3sYear \n%s" %  \
        (" "," ", " "," "," "," "," ",("-"*100)))

    print()
    for i in range(len(lst)):
        data = lst[i]
        name = (data.get_name() [0:15])
        watercourse = (data.get_watercourse() [0:20])
        county = (data.get_county() [0:10])
        state =  (data.get_state() [0:15])
        height = float(data.get_height() [0:10])
        length = float(data.get_length() [0:10])
        year = int(data.get_year() [0:10])

        print("%20s %23s %12s %13s %8.0f %8.0f %7d" % (name, watercourse, \
        county, state, height, length, year))

def printInvalid(lst, search):
    
    if len(lst) == 0:
        if search == 'linear':
            print("\n   Could not find any records matching that location")
        elif search == 'binary':
            print("\n   Could not find any records matching that name")

main()
