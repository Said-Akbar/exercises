# Chapter 4 exercise 11. 12/28/2019 SaidakbarP
# Five-click house
from graphics import *
def main():
    win = GraphWin("Five-click House", 640, 640)
    win.setCoords(0,0,800, 800)

    # get opposite corners of a rectangle with two clicks
    cmd = Text(Point(400,400),"Click two opposite sides of a house frame")
    cmd.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    frame = Rectangle(p1, p2)
    frame.draw(win)

    # get top edge of a door. width is 1/5 of house width. Door reaches the bottom
    cmd.setText("click the top edge of a door")
    door_top = win.getMouse()
    dtop = door_top.getY()
    width = (p2.getX()-p1.getX())/5
    offset = 20
    door = Rectangle(Point(p1.getX()+offset, p1.getY()), Point(p1.getX()+offset + width, dtop))
    door.draw(win)

    # get center of a square window. It is half width of the door
    cmd.setText("Place the window")
    wdw = win.getMouse()
    p1r = Point(wdw.getX()-width/2, wdw.getY()-width/2)
    p2r = Point(wdw.getX()+width/2, wdw.getY()+width/2)
    Rectangle(p1r, p2r).draw(win)

    # get the peak of the roof. Then extend it to top edges of house frame
    cmd.setText("Click the peak of the roof")
    roof = win.getMouse()
    Line(roof, p2).draw(win)
    Line(roof, Point(p1.getX(), p2.getY())).draw(win)

    cmd.setText("")
    win.getMouse()

main()
