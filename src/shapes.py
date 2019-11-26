from Myro import *
from Graphics import *
from colorsys import *
import colorsys


def makeSquare():
    img = Picture(400, 400)
    sq = Rectangle([100, 100], [300, 300])
    show(img, "win")
    win = getWindow("win")
    black = makeColor(0, 0, 0)
    sq.setFill(black)
    win.draw(sq)
    saveWindow("square.png", win)


def makeLine():
    img = Picture(400, 400)
    sq = Line([100, 100], [300, 100])
    show(img, "LINE")
    win = getWindow("LINE")
    black = makeColor(0, 0, 0)
    sq.setFill(black)
    win.draw(sq)
    saveWindow("line.png", win)


makeLine()
