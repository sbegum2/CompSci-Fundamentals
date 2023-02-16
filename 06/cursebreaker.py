"""
  Cursebreaker game

  Samira Begum
  February 2022
"""
from random import choice

def main():

    print_introduction()
    
    rune_list = ["ansuz", "hagalaz", "sowilo", "isaz", "algiz", "ehwaz", "naudiz"]
   
    code = []
    generate_code(rune_list, code)

    for i in range(1,14):    
        print(" ")
        print("============")
        print("Round %d" % (i))
        turn = i
        
        guess = [] 
        get_guess(rune_list, guess)

        print(" ")
        print("You guessed: ")
        print_runes(guess)
        num_matches = check_guess(code,guess)

        is_game_over(num_matches, turn)
        player_won(num_matches)
        test = player_won(num_matches)

        if test == True:
            break

    if test == False:
        print("Sorry, you lose; good thing there's a big stack of cursed \n artifacts!")
    

def print_introduction():
    """
    This function introduces the rules of the game Cursebreaker to the user
    parameters: none
    returns: none
    """
    
    print("\n Welcome to Curse Breaker!")

    print("\n The object of the game for the player is to guess the rune \n sequence, e.g. sowilo isaz hagalaz ansuz. For our game, \n we’ll use 4 runes in the sequence, and we’ll say each rune \n can only show up once (i.e., there are no duplicates in the \n sequence). Each turn, the player enters a guess, and the \n program then reports how many of the player’s guesses are \n correct (using exact matches, meaning the right rune in \n the right place).")
    
    print("\n The player has thirteen turns to guess the secret code. \n If they do, they win! Otherwise, the artifact explodes \n and the evil wizard wins!")

def print_runes(rune_list):
    """
    This function takes a list of strings (rune_list) and prints out the runes
    with vertical bars in between each element in the list
    parameters: rune_list
    returns: nothing
    """

    rune = ""
    for i in range(len(rune_list)):
        rune = rune + rune_list[i] + " | "
    print("")
    print("| " + rune)
    print("")


def get_rune(runes,number):
    """
    This function take a list of the possible runes and a number, and asks the
    user to choose a rune for the numbered position. If the user enters
    something that’s not in the rune list, ask again, and keeps looping until
    the user enters a rune in the list
    parameters: runes, number
    returns: r1
    """

    r1 = input("Enter rune %s: " % (number))

    while r1 not in runes:
        print(r1 + " is not a valid rune.")
        print("Please choose from the following runes: ")
        print_runes(runes)
        r1 = input("Enter rune %s: " % (number))

    return r1


def get_guess(runes, guess):
    """
    This function takes user input to generate a list of the user's 4 guessed
    runes where each entered rune gets added to the list
    parameters: runes, guess
    returns: nothing
    """

    print("Please enter four legal runes. Your choices are: ")
    print_runes(runes)
     
    for i in range(1,5):
        guesses = get_rune(runes, i)
        guess.append(guesses)


def generate_code(runes, code):
    """
    This function chooses 4 random and unique runes from rune_list and
    generates a code of these 4 random elements.
    parameters: runes, code
    returns: code
    """

    L = runes
    while (len(code)) != 4: 
        codePiece = choice(L)

        while codePiece not in code:
            code.append(codePiece)
        else:    
            codePiece = choice(L)
    return code


def check_guess(code,guess):
    """
    This function assesses the user's guesses and checks to see if any of
    the guessed runes are correct and in the right spot in the code sequence.
    It will print how many runes of the 4 exactly match each element of the
    code. If all 4 user-inputted runes match the code, the function prints a 
    congratulatory message.
    parameters: code, guess
    returns: num_matches
    """

    num_matches = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            num_matches += 1
    
    if num_matches != 4:
        print(str(num_matches) + " / 4 correct")
    else: 
        print("Congratulations, you win! The curse is broken!")

    return num_matches

def is_game_over(num_matches, turn):
    """
    This function checks to see if the game is over. If all 4 runes match the
    code or if all 13 rounds have been completed then the game is over. The 
    function will return True if these game over conditions have been met,
    otherwise the function will return False.
    parameters: num_matches, turn
    returns: True or False (depending on conditions met or not)
    """

    if num_matches == 4 or turn > 13:
        return True
    return False


def player_won(num_matches):
    """
    This function checks if the player has won, that is, the user's 
    inputted-runes exactly match the code sequence. If the winning conditions
    have been the met the function will return True and if they haven't, the
    function will return False.
    parameters: num_matches
    returns: True or False (depending on conditions met or not)
    """

    if num_matches == 4:
        return True
    return False
    
main()
