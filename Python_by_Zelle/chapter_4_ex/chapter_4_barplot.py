# Chapter 4 examples and exercises from the python book by John Zelle
from graphics import *
def main():
    print("Plotting a 10 year investment")
    # get inputs
    principal = float(input("Enter the principal: "))
    apr = float(input("Enter the interest rate: "))

    win = GraphWin("10 year investment barplot", 640, 480) # instantiates a window object
    win.setBackground("white") # sets the window background
    win.setCoords(-1.75, -200, 11.5, 10400) # coordinate transformation

    # These lines display x axis ticks
    Text(Point(-1, 0), "0.0K").draw(win) # Text object accepts a coordinate and string literal
    Text(Point(-1, 2500), "0.0K").draw(win)
    Text(Point(-1, 5000), "2.5K").draw(win)
    Text(Point(-1, 7500), "5.0K").draw(win)
    Text(Point(-1, 10000), "7.5K").draw(win)

    # Initial bar plot
    bar = Rectangle(Point(0, 0), Point(1, principal)) # draws a rectangle, requires two points
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # draw bars for each subsequent years
    for year in range(1, 11):
        principal = principal * (1+apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("")
    win.close()
main()
