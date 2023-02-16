"""
  sorting
  Samira Begum
  April 2022
"""
from hydrodam_lab import *

def main():

    data = readData()
    var = getInput()

    myDam = []
    for i in range(len(data)):
        x = data[i].split(",")
        myDam.append(HydroDam(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    update = myDam

    while var != 6:
        var == False
        search = searchsortType(var)
        find = searchInput(var)

        if search == 'quit':
            lst = []
            printInvalid(lst, search)
            print("\n Goodbye! \n")
            break

        elif search == 'state' or search == 'year' or sort == 'sortstate' \
                or sort == 'sortyear' or search == 'reset':
            lst = searching(search, update, find)
            lst = sorting(sorting, update)
            printInvalid(lst, search)
            if len(lst) > 0:
                print()
                printSearch(lst)
        var = getInput()

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
        print("\n \n Please select one of the following choices:")
        search_info = input("\n 1. Filter dams by state name \n 2. Filter dams by year \n 3. Sort by state name \n 4. Sort by year \n 5. Reset list to all dams \n 6. Quit \n Choice? ")
        if search_info == '1' or search_info == '2' or search_info == '3' \
                or search_info=='4' or search_info=='5' or search_info=='6':
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
        search = 'state'
        return search

    elif var == '2':
        valid = True
        search = 'year'
        return search

    elif var == '3':
        valid = True
        sort = 'sortstate'
        return sort

    elif var == '4':
        valid = True
        sort = 'sortyear'
        return sort

    elif var == '5':
        valid = True
        search = 'reset'
        return search

    elif var == '6':
        valid = False
        search = 'quit'
        return search
        print("\n Goodbye!")

def searchInput(var):
    """
    function to get user input on what term to search for in dataset
      
      parameters: var - variable to search for
      returns: find - search term
    """

    if var == '1':
        print()
        find = input(" Location (state)?  ")

    elif var == '2':
        print()
        findmin = int(input(" min year? "))
        findmax = int(input(" max year? "))
        find = [findmin, findmax]

    elif var == '6':
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

    if search == 'state':
        lst = []
        for i in range(len(myDam)):
            if myDam[i].get_state() == find:
                statelst.append(Dam[i])
        return lst

    if search == 'year':
        lst = []
        mini = find[0]
        maxi = find[1]
        for i in range(len(myDam)):
            if myDam[i].get_year() >= mini and myDam[i].get_year() <= maxi:
                yearlst.append(myDam[i])
        return lst

def swap(lst, i, j):
    """
    Function swaps items within a list
      parameters: lst - empty list, i -  one element of the list, j - secondary element of the list
    """
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def sorting(sort, Dam):
    """
    Utilizes a sorting method to update a list
      parameters: search - type of search, Dam - list of dams, statelst yearlst: list of dams according to state or year
      """
    if sort == 'state':

        print("\n Sorted by state \n")

        continued = True
        while continued == True:
            continued = False
            for i in range(len(lst)-1):
                if lst[i+1].get_state() < lst[i].get_state():
                    swap(lst, i , i+1)
                    continued = True
        return lst

    if sort == 'year':
        print("\n Sorted by year \n")
        
        continued = True
        while continued == True:
            continued = False
            for i in range(len(lst)-1):
                if lst[i+1].get_year() < lst[i].get_year():
                    swap(lst, i, i+1)
                    continued = True
        return lst

def printSearch(lst):
    """
    prints user's searched results in a table
    parameters: lst
    returns: none
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
    """
    prints a message when user's search is invalid
    parameters: lst, search
    returns: none
    """
    if len(lst) == 0:
        if search == 'linear':
            print("\n   Could not find any records matching that location")
        elif search == 'binary':
            print("\n   Could not find any records matching that name")

main()
