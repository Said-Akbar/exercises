# exercise 10 from chapter 9. 01/04/2020 by SaidakbarP
# Monte Carlo simulation for pi calculation. This draws a circle circumcribed by a square and calculates the pi by thrown darts
from random import random
from graphics import *

def is_hit(x,y):
    d = ((x-10)**2+(y-10)**2)**(1/2)
    if d>10:
        return 0
    else:
        return 1

def main():
    n = int(input("Enter number of dart throws: "))
    win = GraphWin("pi estimation", 800, 800)
    win.setCoords(0,0,20,20)
    Rectangle(Point(0,0), Point(20,20)).draw(win)
    Circle(Point(10,10), 10).draw(win)

    h = 0
    for i in range(n):
        x = 20*random()
        y = 20*random()
        Point(x,y).draw(win)
        result = is_hit(x,y)
        h += result

    Text(Point(10,10), "done. Click anywhere to exit").draw(win)
    win.getMouse()

    print("Calculated value of pi is: ", round(4*h/n, 4))

if __name__ == '__main__':
    main()
