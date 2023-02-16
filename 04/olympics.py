"""
  Program to summarize the number of medals won by a specific country

  Samira Begum
  February 2022
"""

def main():
    
    print("Let's summarize olympic medals")
    medals = input("Enter medals as a string of g,s, and b, e.g., bggsb: ")

    numG = 0
    numS = 0
    numB = 0

    for i in range(len(medals)):
        if(medals[i] == "g"):
            numG += 1

        elif(medals[i] == "s"):
            numS += 1

        elif(medals[i] == "b"):
            numB += 1
    
    print(" ")
    print("Medal Summary:")
    print(" Gold " + str(numG))
    print(" Silver " + str(numS))
    print(" Bronze " + str(numB))

    if((numG + numS +numB) > 0):
        print("Congratulations!")
        print(" ")

    else:
        print("Better luck in Summer 2024!")
        print(" ")

main()
