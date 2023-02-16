"""
  The Game of Melty

  Samira Begum
  March 2022
"""
from random import *

def main():

    printIntro()
    
    randList = generateWord()

    guessList = list(len(randList)*"-")
    
    guessesLeft = 8

    randList = list(randList)
  
    win = 0
    gameOver = False
    while (gameOver == False or win == 0):

        userInput = getGuess(randList)

        correctGuess = compareGuess(randList, guessList, userInput)
     
        incorrect = determineInc(correctGuess, guessesLeft, guessList) 
        
        if incorrect == False:
            guessesLeft = guessesLeft - 1
            
        print("  Incorrect guesses left: " + str(guessesLeft))
        print(" ")
        
        win = wordGuessed(randList, guessList)
    
        if (win == 1):
            randList = ''.join(randList)
            print("You won! \nThe word was " + str(randList) + "! \nYou saved Melty! :)")
            print(" ")
            break

        elif(guessesLeft == 0):
            randList = ''.join(randList)
            print("Oh no! \nThe word was " + str(randList) + ", \nbut you couldn't guess it in time to save Melty :(")
            print(" ")
            break

#######################################

def printIntro():
    """
    prints information about how to play the Game of Melty
    params: none
    returns: none
    """

    print("\n  This program plays a game of Melty. \n  \n  Guess letters in the mystery word. \n  You can only make 8 incorrect guesses before \n  Melty melts.  See if you can save Melty and \n  guess the word before you run out of guesses. \n \n                  Good Luck! \n")

########################################

def generateWord():
    """
    Opens and reads a file of random words from computer directory, choosing a
     word from this file at random. It then returns the word into a list of the
      letters making up the word
    params: none
    returns: a list consisting of the letters making up the randomly selected word
     (word)
    """

    wordfile = open("/usr/local/doc/wordfile.txt", "r")
    randList = wordfile.readlines()    
    
    word = choice(randList)
    word = word.strip()
    word.split()

    return word

#########################################

def determineInc(correctGuess, guessesLeft, guessList):
    """
    Determines if a guess should be subtracted from the 8 given guesses in main
    params: correctGuess, guessesLeft, guessList
    returns: True or False
    """
    
    if (correctGuess == 0):        
        return False

    return True

#########################################

def getGuess(randList):
    """
    Gets user input of a single character string and checks if string is 
     single character, alphabetical, and lowercase
    params: randList 
    returns: guess
    """
    guess = input("Enter a letter: ")
    
    while not(guess.isalpha() and guess.islower() and len(guess) == 1):
        print("Hey, that's not a single lowercase letter!")
        guess = input("Enter a letter: ")
        print(" ")

    return guess

#########################################

def compareGuess(randList, guessList, userInput):
    """
    Compares userInput at each index to randList to check if the letter at that
     position is equal to the guessed letter. If so, sets correctGuess to 1 
      because guess was correct at least once, and mutates guessList at the 
       corresponding index without returning list

    params: randList, guessList, userInput
    return: correct guess variable. = 1 if userinput was in randlist, 
     = 0 otherwise
    """

    correctGuess = 0
    for i in range(len(randList)):
        if (randList[i] == userInput):
            guessList[i] = userInput
            correctGuess = 1

    if correctGuess == 1:    
        print("  good guess, '" + userInput + "' is in the word")
    
    elif(correctGuess != 1):
        print("sorry there is no '" + userInput + "' in the word")
    
    guess = ""
    for i in range(len(guessList)):
        guess = (guess + guessList[i] + " ")

    print(" ")
    print("word: " + guess)                                                    

    return correctGuess

##########################################

def wordGuessed(randList, guessList):
    """
    Compares mutated guessList to randList in order to determine if all 
    characters in the random list have been guessed.
    
    params: randList, guessList
    returns: wordGuessed = 1 if word is guessed,  = 0 if not
    """
    
    wordGuessed = 0
    charGuessed = 0
    for i in range(len(randList)):
        if (randList[i] == guessList[i]):
            charGuessed = charGuessed + 1
    if (charGuessed == len(randList)):
        wordGuessed = 1

    return wordGuessed

###########################################
main()
