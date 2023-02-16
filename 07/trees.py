"""
  trees.py

  Samira Begum
  March 2022
"""

from graphics import *
from math import sqrt
from random import *

def main():
    
    win = GraphWin("Trees", 800, 800)
    win.setBackground("SkyBlue1")

    make_ground(win)

    sun = make_sun(win)

    while True:
        p = Point(400,750)
        centTxt = Text(p, "Click on the center of the tree")
        centTxt.draw(win)

        click = win.getMouse()
        user_click = distance(win, sun.getCenter(), click)
        
        if user_click <= 30:
            win.close()
        else:
            centTxt.undraw()
            draw_tree(win, click,p)

def make_ground(win):
    """
    This function creates and draws a rectangle at the bottom of the screen to 
    represent the ground.
    Parameters: win (window)
    Returns: None
    """

    p1 = Point(800, 400)
    p2 = Point(0,800)

    ground = Rectangle(p1,p2)
    ground.setFill("forestgreen")
    ground.setOutline("forestgreen")
    ground.draw(win)

def make_sun(win):

    """
    This function creates and draws a circle in the top of the screen to 
    represent the sun.
    Parameters: win (window)
    Returns: sun
    """

    p3 = Point(700,75)
    sun = Circle(p3, 30)
    sun.setFill("gold")
    sun.setOutline("gold")
    sun.draw(win) 

    return sun

def distance(win, click1, click2):
    
    """
    This function calculates the distance between a click and the center of the
    circle.
    Parameters: win, click1, click2)
    Returns: d (distance)
    """

    click1X = click1.getX()
    click1Y = click1.getY()

    click2X = click2.getX()
    click2Y = click2.getY()

    d = sqrt((click1X - click2X)**2 + (click1Y - click2Y)**2)

    return d

def randomColor():
    
    """
    This function chooses three random values for R G and B colors
    Parameters: nothing
    Returns: color_rgb (the random color chosen
    """

    return color_rgb(randrange(255), randrange(255), randrange(255))

def draw_tree(win,p1,p):

    """
    This function guides the user through drawing a tree. It calls for three
    clicks; for the center of the tree, edge of the tree canopy, and base of the 
    tree trunk, creating a circle tree canopy and wide line trunk
    Parameters: win, p1, p
    Returns: None
    """
    
    eTxt = Text(p, "Click on the edge of the tree canopy")
    eTxt.draw(win)
    p2 = win.getMouse()

    eTxt.undraw()
    bTxt = Text(p, "Click on the base of the tree trunk")
    bTxt.draw(win)
    p3 = win.getMouse()
    bTxt.undraw()

    r = distance(win, p2, p1)
    
    leaf = Circle(p1, r)
    leafColor = randomColor()
    leaf.setFill(leafColor)
    leaf.setOutline(leafColor)

    t = sqrt(r)
    
    b = p3.getY()
   
    trunk = Line(p3,p1)
    trunk.setWidth(t)
    trunkColor = randomColor()
    trunk.setFill(trunkColor)
    trunk.setOutline(trunkColor)

    trunk.draw(win)
    leaf.draw(win)

main()
