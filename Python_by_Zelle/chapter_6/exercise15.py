# ex15 chapter 6. 12/28/2019 SaidakbarP
# Drawing smiley faces
from graphics import *
def drawFace(center, size, win):
    radius = round(((center.getX()-size.getX())**2 + (center.getY()-size.getY())**2)**(1/2))
    circle = Circle(center, radius)
    circle.setFill("yellow")
    eye1 = Circle(Point(center.getX()+radius/2,center.getY()+radius/3), radius/5)
    eye1.setFill("red")

    eye2 = eye1.clone()
    eye2.move(-radius, 0)

    mouth = Circle(Point(center.getX(), center.getY()), radius*0.7)

    circle.draw(win)
    mouth.draw(win)
    mouth_cov = Rectangle(Point(mouth.getP1().getX(), mouth.getP1().getY()+radius/3), mouth.getP2())
    mouth_cov.setOutline("yellow")
    mouth_cov.setFill("yellow")
    
    mouth_cov.draw(win)
    eye1.draw(win)
    eye2.draw(win)





def main():
    win = GraphWin("Smiley", 800, 800)
    win.setCoords(0,0,800,800)
    ctr = win.getMouse()
    ctr.draw(win)
    size = win.getMouse()
    size.draw(win)

    drawFace(ctr, size, win)
    win.getMouse()

if __name__== "__main__":
    main()
