from graphics import *
def main():
    win = GraphWin("Move the object", 640, 480)
    shape = Rectangle(Point(200,220), Point(340, 360))
    shape.setOutline("red")
    shape.setFill("green")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2 = shape.clone()
        shape2.move(dx, dy)
        shape2.draw(win)

    txt = Text(Point(320, 240), "Click one more time to quit")
    txt.setSize(25)
    txt.setTextColor("red")
    txt.setStyle('bold')
    txt.draw(win)

    win.getMouse()
    win.close()
main()
