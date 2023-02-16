"""
  flowers.py 

  Samira Begum
  March 2022
"""

from graphics import *

def main():

    n = int(input("Enter number of flowers across: "))
    
    win = GraphWin("Flowers", 800, 800)
    win.setBackground((color_rgb(191, 245, 198)))

    win.setCoords(0,0,n,n)

    for i in range(n):
        for j in range(n):
            draw_flower(win, i, j)

    win.getMouse()
    win.close()

def draw_flower(win, row, col):

    """
    This function draws the five circles that make up one flower in a 1x1
    Parameters: win, row, col
    Returns: None
    """

    w1 = Circle(Point(.4 + row, .4 + col), .2)
    w1.setOutline("white")
    w1.setFill("white")
    w1.draw(win)

    b2 = Circle(Point(.6 + row, .6 + col), .2)
    b2.setOutline("white")
    b2.setFill("white")
    b2.draw(win)


    w2 = Circle(Point(.4 + row, .6 + col), .2)
    w2.setOutline("turquoise3")
    w2.setFill("turquoise3")
    w2.draw(win)

    b1 = Circle(Point(.6 + row, .4 + col), .2)
    b1.setOutline("turquoise3")
    b1.setFill("turquoise3")
    b1.draw(win)

    center = Circle(Point(.5 + row, .5 + col), .075)
    center.setOutline("gold")
    center.setFill("gold")
    center.draw(win)

main()
