# exercise 2 from chapter 10. 01/25/2020 by SaidakbarP
# button class
from graphics import *

class Button:
    """a button to do actions on GUI"""
    def __init__(self, win, center, width, height, label):
        w, h = width/2.0, height/2.0 # button w and h divided by 2 because we calculate from center
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w # add w to get x max; subtract w to get x min
        self.ymax, self.ymin = y+h, y-h # get y max and y min
        p1 = Point(self.xmin, self.ymin) # based on x min and y min, create the p1 of a Rectangle
        p2 = Point(self.xmax, self.ymax) # create p2 of a Rectangle
        self.rect = Rectangle(p1, p2) # button itself
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label) # place button label
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """checks whether the button was clicked"""
        if p == None: return False
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
                # returns true when button is active, and mouse clicked is within button boundaries
    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
