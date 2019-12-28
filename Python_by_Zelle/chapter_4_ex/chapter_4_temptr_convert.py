# Chapter 4 examples and exercises from the python book by John Zelle
from graphics import *
def main():
    print("Celsius to Fahrenheit converter")
    win = GraphWin("Celsius to Fahrenheit", 640, 480) # instantiate the window
    win.setCoords(0.0, 0.0, 3.0, 4.0) # Transform the coordinates

    Text(Point(1, 3), " Celsius Temperature: ").draw(win) # draw text with a string literal
    Text(Point(1,1), "Fahrenheit Temperature: ").draw(win)
    inputText = Entry(Point(2.25, 3), 5)                   # an input form in the window
    inputText.setText("0.0") # default text in the input form
    inputText.draw(win)
    outputText = Text(Point(2.25,1),"")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    win.getMouse()

    celsius = float(inputText.getText())
    fahrenheit = 9/5*celsius + 32

    outputText.setText(round(fahrenheit,2))
    button.setText("Quit")

    win.getMouse()
    win.close()

main()
