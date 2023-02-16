"""
TODO: write menagerie program (should use Critter class in critter.py)
"""

from critter import *

def main():
    
    menu = getInput()
    initial = None
    
    while menu != '0':
    
        menu = getInput()

        if menu == '2':
            initial = True
        else: 
            intial = False

        if menu == '0':
            print("\n Goodbye!")
            break

        elif menu == '1':
            if initial == True:
                check(lst_critters)
            else:
                print("\n There are no critters to check on. Try adding some!")
    
        elif menu == '2':
            lst_critters = addNew()
            
        elif menu == '3':
            if initial == True:
                feed(lst_critters)
            else:   
                print("\n There are no critters to feed. Try adding some!")

        elif menu == '4':
            if initial == True:
                pet(lst_critters)
            else:
                print("\n There are no critters to pet. Try adding some!")
    
        elif menu == '5':
            if initial == True:            
                play(lst_critters)
            else:
                print("\n There are no critters to play with. Try adding some!")

        elif menu == '6':
            if initial == True:
                sleep(lst_critters)
            else:
                print("\n There are no critters to put to bed. Try adding some!")


def getInput():
    print("\n" + 20*"-" + "\n Main Menu:")
    valid = False
    while valid == False:
        menu = input("\n  1. Check on critters \n  2. Add new critters \
            \n  3. Feed critter \n  4. Pet critter \n  5. Play with critter \
            \n  6. Go to bed \n  0. Quit \n \n  Enter selection: ")
        if menu == '0' or menu == '1' or menu == '2' or menu == '3' \
                or menu=='4' or menu=='5' or menu=='6':
            valid = True
        else:
            valid = False
            print("\n \n  Invalid selection, please try again: ")
            menu = input("\n  1. Check on critters \n  2. Add new critters \
            \n  3. Feed critter \n  4. Pet critter \n  5. Play with critter \
            \n  6. Go to bed \n  0. Quit \n \n Enter selection: ")

    return menu

def check(lst_critters):

    if len(lst_critters) >= 1 and len(lst_critters) <= 4:
        print("The room has some critters in it:")
        
        for i in range(len(lst_critters)):
            print(lst_critters[i][0] + " is " + lst_critters[i][1] + \
                    __str__(critter))
    
    elif(len(lst_critters)) > 4:
        print("The room is full of critters!")
    else:
        print("No critters here yet; try adding one!")

def addNew():
    
    lst_critters = []

    crit = Critter("","","","","")

    name = input("\n New critter's name: ")
    #crit.set_name = input("\n New critter's name: ")

    desc = input(" What's an adjective that describes the critter?: ")
    #crit.set_desc = input(" What's an adjective that describes the critter?: ")
    
    personal = input(" What's the critter's personal pronoun (e.g. she, they, it)?: ")
    #crit.set_personal = input(" What's the critter's personal pronoun (e.g. she, they, it)?: ")
    
    possesive = input(" What's the critter's posessive pronoun (e.g. her, their, its)?: ")
    #crit.set_possesive = input(" What's the critter's posessive pronoun (e.g. her, their, its)?: ")
   
    eat = input(" What does the critter like to eat?: ")
    #crit.set_eat = input(" What does the critter like to eat?: ")
        
    crit = Critter(name,desc,personal,possesive,eat)

    lst_critters.append(crit)
    
    return lst_critters

def feed(lst_critters):

    print("Available critters: ")
    print(len(lst_critters))
    print(lst_critters)

    length = (len(lst_critters))

    for i in range(length):
        print("  " + str(i) + ". " + Critter(name))

    choice = input("Please select a critter: ")
    
def pet(lst_critters):
    
    Critter(pet)
    print(str(lst_critters[0][0]))

def play(lst_critters):
    
    Critter(play)

def sleep(lst_critters):
    
    Critter(sleep)

main()
