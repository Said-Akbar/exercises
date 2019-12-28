# ex 7 Circle Intersection. Created by SaidakbarP 12/24/2019
from graphics import *
def main():
    #r = int(input("Enter Radius of the circle: "))
    win = GraphWin("Circle Intersection", 640, 640)
    win.setCoords(-10, -10, 10, 10)

    # entry box for radius
    radius_entry = Entry(Point(-3, 9), 10)
    radius_entry.setText("7.0")
    radius_entry.draw(win)
    Text(Point(-7, 9), "Enter radius (x<10): ").draw(win)

    # entry box for y-intercept
    y_int = Entry(Point(-3, 8), 10)
    y_int.setText("-3.0")
    y_int.draw(win)
    Text(Point(-7, 8), "Enter y-intercept (y<10) : ").draw(win)

    Rectangle(Point(-1, 7.7), Point(2, 8.8)).draw(win)
    button = Text(Point(0.5, 8.2), "Calculate!")
    button.draw(win)
    # get values
    win.getMouse()
    r = float(radius_entry.getText())
    y = float(y_int.getText())

    # draw circle
    circle = Circle(Point(0,0), r)
    circle.draw(win)

    # draw line
    y_ints = Line(Point(-10,y), Point(10,y))
    y_ints.draw(win)

    # Intersections x-values
    x1 = -round((r**2-y**2)**(1/2))
    x2 = round((r**2-y**2)**(1/2))
    # draw intersections
    Text(Point(x1+0.5,y-0.5), "x1: {}".format(x1)).draw(win)
    win.plot(x1, y, "red")
    Text(Point(x2+0.5,y-0.5), "x2: {}".format(x2)).draw(win)
    win.plot(x2, y, "red")

    button.setText("Quit!")
    win.getMouse()
    win.close()
main()
