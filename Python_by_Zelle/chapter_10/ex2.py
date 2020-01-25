# exercise 2 chapter 10, 01/25/2020 by SaidakbarP
# Graphical representation of a random walk
from random import random
from graphics import *
import math
from button import Button

def new_pos(x,y,angle):
    x = x + math.cos(angle)
    y = y + math.sin(angle)
    return x, y

def createEntry(x, y, win, desc): # create entry
    cmd = Text(Point(x, y), desc)
    str_ = Entry(Point(x+150, y), 15)
    cmd.draw(win)
    str_.draw(win)
    return str_

def main():
    #n = int(input("Enter the number of steps: "))
    win = GraphWin("Random walk simulation", 800, 800)
    win.setCoords(0,0,800,800)
    entry = createEntry(50, 750, win, "Steps:")
    okbutton = Button(win, Point(300, 750), 50, 25, "OK")
    okbutton.activate()
    pt = win.getMouse()
    while not okbutton.clicked(pt):
        pt = win.getMouse()
    okbutton.deactivate()
    quitbutton = Button(win, Point(600,750), 50,25, "STOP")
    quitbutton.activate()

    n = int(entry.getText())
    x, y = 400, 400 # start in the center
    for i in range(n):
        pt = win.checkMouse()
        if quitbutton.clicked(pt): # check for quit button each loop
            break
        x0, y0 = x, y
        angle = random()*2*math.pi
        x, y = new_pos(x, y, angle)
        if 0<=x<800 and 0<=y<800:
            Line(Point(x0,y0), Point(x,y)).draw(win)
        else:
            x=x0
            y=y0
    quitbutton = Button(win, Point(600,750), 50,25, "QUIT")
    quitbutton.activate()
    pt = win.getMouse()
    while not quitbutton.clicked(pt):
        pt = win.getMouse()

if __name__ == '__main__':
    main()
