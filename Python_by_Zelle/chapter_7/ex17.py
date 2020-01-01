# exercise 16, chapter 7, 01/01/2020 by SaidakbarP
# A simple program that displays a bouncing ball
from graphics import *
def main():
    win = GraphWin("Ball", 640, 480)
    win.setCoords(0, 0, 640, 480)
    txt = Text(Point(170,450), "Click on the screen to initiate the ball location")
    txt.draw(win)

    ballp = win.getMouse()
    ball = Circle(ballp, 20)
    ball.setFill("yellow")
    ball.draw(win)
    txt.undraw()
    dx, dy = 1, 1
    x = ballp.getX()
    y = ballp.getY()

    #for i in range(1000):
    while True:
        ball.move(dx,dy)
        if ball.getCenter().getX()>640:
            dx = -1
        elif ball.getCenter().getX()<0:
            dx = 1
        if ball.getCenter().getY()>480:
            dy = -1
        elif ball.getCenter().getY()<0:
            dy = 1
        pt = win.checkMouse()
        if pt:
            break
        update(100)
        
    txt.setText("click anywhere to quit")
    txt.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
