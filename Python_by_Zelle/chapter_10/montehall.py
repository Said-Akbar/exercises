# exercise 3, chapter 10. 01/25/2020 by SaidakbarP
# Monte Hall problem in graphical representation
# the class should draw three doors on the window, and randomly select one.
# then user should seect one door and after selection, the program should show
# whether the choice was correct.
from graphics import *
from button import Button
from random import randrange

class Montehall:
    def __init__(self, win, x, y):
        self.upperY = int(y*0.8)
        self.lowerY = int(y*0.15)
        self.xmax = int(x*0.95)
        self.xmin = int(x*0.05)
        self.door_section = (self.xmax-self.xmin)//3
        self.win = win

        self.door1 = self.__drawdoor(1)
        self.door2 = self.__drawdoor(2)
        self.door3 = self.__drawdoor(3)
    def set_value(self, rd):
        self.door_chosen = rd
        #print(self.door_chosen)
    def __drawdoor(self, n):
        offset = self.xmin*0.5
        p1 = Point(self.xmin + self.door_section*(n-1)+offset, self.lowerY+offset)
        p2 = Point(self.xmax - self.door_section*(3-n)-offset, self.upperY-offset)
        rect = Rectangle(p1, p2)
        rect.setFill("brown")
        rect.draw(self.win)
        return rect

    def door_clicked(self, pt):
        if pt == None: return False
        if (self.door1.getP1().getX() <= pt.getX() <= self.door1.getP2().getX() and
            self.door1.getP1().getY() <= pt.getY() <= self.door1.getP2().getY()):
            self.door_color(self.door1, 1)
            return 1
        if (self.door2.getP1().getX() <= pt.getX() <= self.door2.getP2().getX() and
            self.door2.getP1().getY() <= pt.getY() <= self.door2.getP2().getY()):
            self.door_color(self.door2, 2)
            return 2
        if (self.door3.getP1().getX() <= pt.getX() <= self.door3.getP2().getX() and
            self.door3.getP1().getY() <= pt.getY() <= self.door3.getP2().getY()):
            self.door_color(self.door3, 3)
            return 3
        return False
    def door_color(self, door, n):
        if self.door_chosen == n:
            door.setFill('green')
        else:
            door.setFill('black')

def main():
    x = y = 800
    win = GraphWin("Monte Hall doors", x, y)
    win.setCoords(0,0, x, y)

    quitbutton = Button(win, Point(600,750), 50,25, "QUIT")
    quitbutton.activate()
    txt = Text(Point(400,750), "correctly guessed: {:>5}".format(0))
    txt.draw(win)
    #pt = win.getMouse()
    dr = Montehall(win,x,y)
    guessed = 0
    total = 0
    while True:
        pt = win.getMouse()
        if quitbutton.clicked(pt): # check for quit button each loop
            break
        random_door = randrange(1,4)
        dr = Montehall(win,x,y)
        dr.set_value(random_door)
        #pt = win.getMouse()
        dr_n = dr.door_clicked(pt)
        while not dr_n:
            if quitbutton.clicked(pt): # check for quit button each loop
                break
            pt = win.getMouse()
            dr_n = dr.door_clicked(pt)
        if dr_n == random_door:
            guessed += 1
        total += 1
        txt.setText("correctly guessed: {0:>5}   /{1:>5}".format(guessed, total))
        #print(random_door, dr_n)

    #win.getMouse()

if __name__ == '__main__':
    main()
