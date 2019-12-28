from graphics import *
def main():
    win = GraphWin("Dart", 640, 480)
    win.setCoords(0, 0, 640, 480)

    colors = ['white', 'black', 'blue', 'red']
    r = 50
    rx = r * 4
    for color in colors:
        center = Circle(Point(320, 240), rx)
        center.setFill(color)
        center.draw(win)
        rx = rx - r

    hit = win.getMouse()
    Point(hit.getX(), hit.getY()).draw(win)
    txt=Text(Point(hit.getX(), hit.getY()), "you hit here")
    txt.setSize(24)
    txt.setStyle("bold")
    txt.draw(win)

    win.getMouse()

    win.close()
main()
