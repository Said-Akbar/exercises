# exercise 14 from chapter 8. 01/01/2020 by SaidakbarP
# This program converts color image to grayscale
from graphics import *

def createButton(x, y, win, txt): # creates a button with text
    rct = Rectangle(Point(x, y), Point(x+80, y+20))
    rct.draw(win)
    form = Text(Point(x+40,y+11), txt)
    form.draw(win)
    return rct, form

def buttonClicked(point, rct): # check if the button is clicked
    p1, p2 = rct.getP1(), rct.getP2()
    if p1.getX() <= point.getX() <= p2.getX() and p1.getY()<=point.getY()<=p2.getY():
        return False
    return True

def createEntry(x, y, win, desc): # create entry
    cmd = Text(Point(x, y), desc)
    path = Entry(Point(x+150, y), 15)
    cmd.draw(win)
    path.draw(win)
    return path

def convert(img):
    cols = img.getWidth()
    rows = img.getHeight()
    #print(rows, cols) # 600 800
    for row in range(rows):
        #img.undraw()
        for col in range(cols):
            #print(row,col)
            r, g, b = img.getPixel(col, row)
            brightness = int(round(0.299*r+0.587*g+0.114*b))
            img.setPixel(col, row, color_rgb(brightness, brightness, brightness))
            #update(30)
        update()
    return img

def main():
    win = GraphWin("color->grayscale", 800, 800)
    win.setCoords(0,0,800,800)

    # DONE button
    rct, form = createButton(600,750,win,"DONE")
    # create entry for path
    path = createEntry(120,750, win, "Enter Image Name: ")
    okInput, _ = createButton(350, 740, win, "OK")

    # wait for image path
    point = win.getMouse()
    while buttonClicked(point, okInput):
        point = win.getMouse()
    infile = path.getText()
    # show image on screen
    img = Image(Point(400,375), infile)
    img.draw(win)

    form.setText("CONVERT")
    point = win.getMouse()
    while buttonClicked(point, rct):
        point = win.getMouse()

    outimg = convert(img)

    # create entry for output
    out = createEntry(120, 720, win, "Enter Output Name: ")
    okOut, _ = createButton(350, 710, win, "OK")
    # wait for output filename
    point = win.getMouse()
    while buttonClicked(point, okOut):
        point = win.getMouse()
    # save image
    outimg.save(out.getText())

    # quit button
    form.setText("QUIT")
    point = win.getMouse()
    while buttonClicked(point, rct):
        point = win.getMouse()

if __name__ == '__main__':
    main()
