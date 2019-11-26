from Myro import *
from Graphics import *

t = 0
linePic = Picture("sq.png")
newPic = Picture(linePic)
show(linePic, "Original")
show(newPic, "New")

for i in range(linePic.width):
    for j in range(linePic.width):
        rX1, gX1, bX1 = linePic.getRGB(i, j)
        rX2, gX2, bX2 = linePic.getRGB(i - 1, j)
        rY1, gY1, bY1 = linePic.getRGB(i, j)
        rY2, gY2, bY2 = linePic.getRGB(i, j - 1)
        gX1 = (rX1 + gX1 + bX1) / 3.0
        gX2 = (rX2 + gX2 + bX2) / 3.0
        gY1 = (rY1 + gY1 + bY1) / 3.0
        gY2 = (rY2 + gY2 + bY2) / 3.0
        # print("G1", g1)
        # print("G2", g2)
        contrastX = gX1 - gX2
        contrastY = gY1 - gY2
        # print(contrast)
        # print("Difference:",g1 - g2)

        if contrastX != 0 or contrastY != 0:
            if abs(contrastX) == 255 or abs(contrastY) == 255:
                # print(contrastX)
                # print("foo")
                newPic.setRGB(i - t, j, 255, 0, 255)
