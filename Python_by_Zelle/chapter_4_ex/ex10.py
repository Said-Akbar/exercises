# ex 10 Triangle Information. Created by SaidakbarP 12/24/2019
from graphics import *
def perimeter(point1, point2):
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    length = (dx**2 + dy**2)**(1/2)
    return length

def main():
    win = GraphWin("Circle Intersection", 640, 640)
    win.setCoords(0, 0, 20, 20)
    Text(Point(4, 19), "Set three points to create a triangle").draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("green")
    triangle.draw(win)
    Text(p1, "{}, {}".format(round(p1.getX()), round(p1.getY()))).draw(win)
    Text(p2, "{}, {}".format(round(p2.getX()), round(p2.getY()))).draw(win)
    Text(p3, "{}, {}".format(round(p3.getX()), round(p3.getY()))).draw(win)
    # perimeter calculation
    a = perimeter(p1, p2)
    b = perimeter(p2, p3)
    c = perimeter(p3, p1)
    total_p = a + b + c

    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)

    Text(Point(4, 18), "Perimeter is: {} \nArea is: {}".format(round(total_p), round(area))).draw(win)

    txt = Text(Point(10,3), "Click anywhere to quit")
    txt.setSize(24)
    txt.draw(win)
    win.getMouse()
    win.close()

main()
