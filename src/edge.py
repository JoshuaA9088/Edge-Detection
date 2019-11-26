from Myro import *
from Graphics import *

linePic = Picture("img.jpg")
show(linePic)
newPic = Picture(linePic)
show(linePic, "Original")
show(newPic, "New")

for i in range(linePic.width):
    for j in range(linePic.height):
        rX1, gX1, bX1 = linePic.getRGB(i, j)
        rX2, gX2, bX2 = linePic.getRGB(i + 1, j)
        rY1, gY1, bY1 = linePic.getRGB(i, j)
        rY2, gY2, bY2 = linePic.getRGB(i, j + 1)

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

        if abs(contrastX) != 0 or abs(contrastY) != 0:
            # print(contrast)
            newPic.setRGB(i, j, 255, 0, 255)
