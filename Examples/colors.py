from Myro import *
from Graphics import *

img = Picture(200,200)
show(img, "img")
win = getWindow("img")
c = Circle((100, 100), 20)
green = makeColor(  0, 255,   0)
c.setColor(green)
c.draw(win)