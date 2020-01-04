# exercise 14 from chapter 9. 01/04/2020 by SaidakbarP
# Graphical representation of a random walk
from random import random
from graphics import *
import math

def new_pos(x,y,angle):
    x = x + math.cos(angle)
    y = y + math.sin(angle)
    return x, y

def main():
    n = int(input("Enter the number of steps: "))
    win = GraphWin("Random walk simulation", 800, 800)
    win.setCoords(0,0,100,100)
    x, y = 50, 50
    for i in range(n):
        x0, y0 = x, y
        angle = random()*2*math.pi
        x, y = new_pos(x, y, angle)
        if 0<=x<100 and 0<=y<100:
            Line(Point(x0,y0), Point(x,y)).draw(win)
        else:
            x=x0
            y=y0
    win.getMouse()

if __name__ == '__main__':
    main()
