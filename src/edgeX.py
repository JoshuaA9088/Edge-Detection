from Myro import *
from Graphics import *

linePic = Picture("shapes.jpg")
newPic = Picture(linePic)
show(linePic, "Original")
show(newPic, "New")
win = getWindow("New")

for i in range(linePic.width):
    for j in range(linePic.height):
        rX1, gX1, bX1 = linePic.getRGB(i, j)
        rX2, gX2, bX2 = linePic.getRGB(i + 1, j)

        contrastX = gX1 - gX2
        # print(contrastY)
        if contrastX != 0:
            # print(contrastY)
            if abs(contrastX) >= 80 or abs(contrastX) <= 0:
                if contrastX < 0:
                    newPic.setRGB(i + 1, j, 255, 0, 255)
                else:
                    newPic.setRGB(i, j, 255, 255, 0)
