# ex16 chapter 6. 12/28/2019 SaidakbarP
# Drawing smiley faces on photo images
from graphics import *
def drawFace(center, size, win):
    radius = round(((center.getX()-size.getX())**2 + (center.getY()-size.getY())**2)**(1/2))
    circle = Circle(center, radius)
    circle.setFill("yellow")
    eye1 = Circle(Point(center.getX()+radius/2,center.getY()+radius/3), radius/5)
    eye1.setFill("red")

    eye2 = eye1.clone()
    eye2.move(-radius, 0)

    mouth = Circle(Point(center.getX(), center.getY()), radius*0.7)

    circle.draw(win)
    mouth.draw(win)
    mouth_cov = Rectangle(Point(mouth.getP1().getX(), mouth.getP1().getY()+radius/3), mouth.getP2())
    mouth_cov.setOutline("yellow")
    mouth_cov.setFill("yellow")

    mouth_cov.draw(win)
    eye1.draw(win)
    eye2.draw(win)





def main():
    win = GraphWin("Smiley", 800, 800)
    win.setCoords(0,0, 800, 800)

    cmd = Text(Point(120, 750), "Enter image name: ")
    cmd.draw(win)

    path = Entry(Point(280,750), 15)
    path.setText("*.gif")
    path.draw(win)
    Text(Point(380, 750), "Ok").draw(win)
    win.getMouse()

    #Rectangle(Point(50,50), Point(750, 700)).draw(win)
    img = Image(Point(400,375), path.getText())
    img.draw(win)

    Text(Point(120, 720), "N faces in image: ").draw(win)
    faces = Entry(Point(280,720), 15)
    faces.setText("1")
    faces.draw(win)
    Text(Point(380, 720), "Ok").draw(win)
    win.getMouse()

    for face in range(int(faces.getText())):
        ctr = win.getMouse()
        ctr.draw(win)
        size = win.getMouse()
        size.draw(win)

        drawFace(ctr, size, win)

    Text(Point(350, 50), "Save Image").draw(win)
    win.getMouse()
    #img.save("smiley.gif")

    Text(Point(350,20), "Quit").draw(win)
    win.getMouse()

if __name__== "__main__":
    main()
