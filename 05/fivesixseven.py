"""
fivesixseven:

    Samira Begum
    February 2022
"""

from random import *

def main():

    print(" ")
    name = input("Enter your name: ")
    printWelcome(name)

    print("Enter the number of rounds you'd like to play (30 max): ")
    rounds = getNumBetween(1,30)
    int(rounds)

    wins = 0

    for i in range(rounds):
        print(" ")
        print("Let's start round " + str(i+1))
        wins = PlayOneRound(name,wins)

    printResults(wins,rounds,name)

def printWelcome(name):

    """
    This function Introduces the player to the function and rules of the game 
    Five-Six Seven
    parameters: user input name
    returns: nothing
    """

    print(" ")
    print("Hi " + name + " and welcome to the game of 5-6-7!")
    print("Each round you pick a number between 0 and 5 inclusive.")
    print("and the computer picks a number between 0 and 5 inclusive.")
    print("If the total of the two values is between 5 and 7 inclusive")
    print("you win!  If not, the computer wins. :(  ")
    print("At the end of all the rounds, I'll print out your win percentage")
    print(" ")
    print("Good luck!")
    print(" ")

def getNumBetween(low,high):

    """
    This function that takes two int values represented the low and the high 
      ends of a range of values (inclusive), and returns a value entered by the 
      user that is between that range
    parameters: user input integer between 1 and 30
    retuns: number of rounds
    """
    rounds = int(input("Enter a value between 1 and 30: "))
    
    while(rounds < 1 or rounds > 30):
        print("hey! " + str(rounds) + " is not between 1 and 30 try again...")
        rounds = int(input("Enter a value between 1 and 30: "))

    else:
        return rounds

def printResults(x, y, n):
    
    """
    This function displays the summary statistics of the game, which include:
      the number of games the human player won out of the total played, the
      percentage of games won by the human, and an overall win/loss message
    parameters: number of games won by human player, total number of rounds
      played, player's name
    returns: nothing
    """

    print(" ")
    print(n + ", you won %d out of %d times" % (x,y))
    percent = (x/y)
    print("for a winning percentage of " + str("%.2f" % (percent)))
       
    if(percent > .50):
        print("You beat the computer. Yay!")
        print(" ")
    elif(percent == .50):
        print("You tied with the computer! Try playing again.")
        print(" ")
    else:
        print("The computer beat you. Better luck next time!")
        print(" ")

def PlayOneRound(name, wins):

    """
    This function goes through one round of the game and repeats for as many
      rounds as the user specified
    parameters: user input name
    returns: total wins
    """

    print(" ")
    print(name + " you get to start this round by picking a number")
    val = int(input("Enter a value between 0 and 5: "))
   

    while(val < 0 or val > 5):
        print("hey, " + str(val) + " isn't between 0 and 5")
        val = int(input("Enter a value between 0 and 5: "))

    compVal = randrange(0,5)
    
    total = compVal + val

    print("  you chose " + str(val) + " and the computer chose " + str(compVal))
    
    if(total < 5 or total > 7):
        print("  Sorry, you lose this round!")

    else:
        print("  You win this round!")
        wins += 1

    return wins
    #print("Debug: call to PlayOneRound returned: " + str(winner)) 
    print("...")

main()
