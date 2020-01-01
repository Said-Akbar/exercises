# exercise 16, chapter 7, 01/01/2020 by SaidakbarP
# A simple program that displays an archery target and collects scores from clicked points
from graphics import *
def points(hit):
    # to calculate if the point is inside a circle, we need to calculate the distance between point and circle's center
    X = hit.getX()
    Y = hit.getY()
    centerX = 320
    centerY = 240

    distance = ((centerX-X)**(2)+(centerY-Y)**(2))**(1/2)
    point = 0
    if distance<50:
        point = 9
    elif 50<=distance<100:
        point = 7
    elif 100<=distance<150:
        point = 5
    elif 150<=distance<200:
        point = 1

    return point

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
    score = 0
    txt=Text(Point(70,400), "Your score is: {}".format(score))
    txt.draw(win)

    for i in range(5):
        hit = win.getMouse()
        Point(hit.getX(), hit.getY()).draw(win)
        score = score + points(hit)
        txt.setText("Your score is: {}".format(score))

    win.getMouse()

    win.close()

if __name__ == '__main__':
    main()
