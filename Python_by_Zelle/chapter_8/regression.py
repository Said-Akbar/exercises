# exercise 13 from chapter 8. 12/30/2019 by SaidakbarP
# Linear regression graph
from graphics import *

def notDone(point):
    if 300<=point.getX()<=400 and 750<=point.getY()<=780:
        return False
    return True

def regression(y_vals, x_vals):
    x_bar = sum(x_vals)/len(x_vals)
    y_bar = sum(y_vals)/len(y_vals)
    s_xy = []
    s_x = []

    for i in range(len(x_vals)):
        s_xy.append((x_vals[i]-x_bar)*(y_vals[i]-y_bar))
        s_x.append((x_vals[i]-x_bar)**2)

    beta = sum(s_xy)/sum(s_x)
    alpha = y_bar - beta*x_bar

    y1 = alpha + beta * 100
    y2 = alpha + beta * 700

    return Point(100, y1), Point(700, y2), alpha, beta

def main():
    win = GraphWin("Regression graph", 800, 800)
    win.setCoords(0,0,800,800)

    # DONE button
    Rectangle(Point(300, 750), Point(400, 780)).draw(win)
    form = Text(Point(350,765), "DONE")
    form.draw(win)

    y_vals = []
    x_vals = []
    point = win.getMouse()
    v = point.clone()
    v.draw(win)
    t = Text(Point(110, 700),"Equation: y = {:4.2f} + {:4.2f} * x".format(0, 0))
    t.draw(win)
    # get points
    while notDone(point):
        point.draw(win)
        y_vals.append(point.getY())
        x_vals.append(point.getX())
        point = win.getMouse()
        if len(y_vals)>3:
            v.undraw()
            point1, point2, alpha, beta = regression(y_vals, x_vals )
            t.setText("Equation: y = {:4.2f} + {:4.2f} * x\nPoints collected: {}".format(alpha, beta, len(y_vals)))
            v = Line(point1, point2)
            v.draw(win)

    # Quit button
    form.setText("QUIT")
    point = win.getMouse()
    while notDone(point):
        point = win.getMouse()

if __name__ == '__main__':
    main()
