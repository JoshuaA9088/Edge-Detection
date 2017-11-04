from Myro import *
from Graphics import *
from colorsys import *
import colorsys

def makeSquare():
    img = Picture(400, 400)
    sq = Rectangle([100, 100],[300,300])
    show(img, "win")
    win = getWindow("win")
    black = makeColor(0,0,0)
    sq.setFill(black)
    win.draw(sq)
    #savePicture(win, "sq.jpg")
    win.saveTojpg("foo.svg")
makeSquare()