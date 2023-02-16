"""
 TDD for the Game of Melty

 Samira Begum, Kat Schmidt
 March 2022
"""
from random import *

def main():

#1 print instructions 
    """
    calls function printIntro to print information about the game
    """
#2 generate random word, create list with character entries
    """
    call function generateWord to pick random word from wordfile.txt and stores
    randomly generated word as a list of single letter strings in main

    this list is referred to as randlist moving forward and should not be mutated
    """
    randlist = generateWord()

#3 generate list with entries = length of random word (guess list)
    """
    creating a new list (currently all "-" entries) of characters to be guessed
    use a for loop to append "-" character to guess list for each character
    in random list. List referred to as guesslist moving forward and will be
    mutated during the game to update "-" entries with correctly guessed chars

    use a for loop (for i in range len(randlist)) to set up initial list as the
    correct length
    """
    guesslist = []

#4 set guesses left = 8
    guessesleft = 8

#5 while loop runs as long as guesses left > 0 with steps to play melty or if user /n correctly guesses the word
    #i run printGameInfo with params guesses left, guesslist to update player
        #on the current status of the game
    #ii create variable userinput = getguess()
    userinput = getGuess()
    #iii compare guessed letter to randlist using function 
        #compareguess(userinput, randlist, guesslist)
        #guesscorrect = compareguess will create a variable describing if the
        #user inputted character was in the randlist
    guesscorrect = compareGuess()
    #iv create variable  guessed = the return of the wordguessed function
        #wordguessed(randlist, guesslist)  (guesslist mutated by compareguess)
        #this variable describes if the randlist and guesslist match
    guessed = wordGuessed()
    #v adjust guessesleft variable using endgame function. Should reduce
        #guessesleft by 1 if guesscorrect returned 0 or reduce guessesleft to 0
        #to end game if randlist and guesslist match and wordguessed returned
        #1 guesscorrect(guessesleft, guesscorrect, guessed)
    guessesleft = 0
#6 after while loop runs to completion, print appropriate exit message
    #i if guessed == 1 print win statement 
    #ii if guessed == 0 print loss statement, this statement should include the
        #randomly selected word as a string, made from using join method on 
        #randlist


def printIntro():
    """
    simple print function to print information about how the game is played."
    no params, no return
    """
    
    print("")

def generateWord():
    """
    params: wordfile.txt
    returns: randomly selected word, converted into a list of single letter strings
    """
    #i open wordfile.txt
    #ii create list using readlines method
    #iii strip selected word using strip method
    #iv split selected word string into a list using split method
    #v return random word list
    
    return []

def printGameInfo():
    """
    params: incorrect guesses left, guesslist
    returns: nothing
    function should print out the number of incorrect guesses left and the 
    current status of the guess list. For visual appeal, convert guesslist
    into a string format
    """

    print("")

def getGuess():
    """
    params: none 
    returns: userinput
    function gets user input of a single character string and checks if string
    is single character and alphabetical
    """
    #i guess = input(prompt)
    #ii while loop, continue prompting user for input while the previous input
        #is not appropriate
    #iii return appropriate input 

    return ""

def compareGuess():
    """
    params: randlist, guesslist, userinput
    return: correct guess variable. = 1 if userinput was in randlist, = 0 otherwise
    compares userinput at each index to randlist to check if the letter at that
    position is equal to the guessed letter. If so, sets correctguess to 1 because
    guess was correct at least once, and mutates guesslist at the corresponding
    index without returning list
    """
    #i set correctguess to 0 by default
    #ii for loop checks randlist and each index 
    """
    for i in range(len(randlist)):
        if randlist[i] == userinput:
            guesslist[i] == userinput
            correctguess = 1
    """
    #return correctguess to main function
    
    return 0

def wordGuessed():
    """
    compares mutated guesslist to randlist in order to determine if all characters
    in the random list have been guessed
    params: guesslist, randlist
    returns: guessed variable = 1 if word guessed = 0 if not
    """
    #i set correct characters and guessed = 0
    #ii for loop checks randlist[i] == guesslist[i], i in the length of both lists
    #iii if randlist[i] == guesslist[i] add 1 to correct characters accumulator
    #iv check if correct characters = length of both lists. if yes return 1

    return 0
