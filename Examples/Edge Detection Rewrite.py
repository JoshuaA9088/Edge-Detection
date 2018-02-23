from Myro import *
from Graphics import *
import Math

pic = Picture("blockG2.png")

def findEdge(pic):
    newPic = Picture(pic)
    thresh1 = 1000
    thresh2 = 25
    avoidX = [0, 1, 2, 3, 4, 5, (pic.width - 1), (pic.width - 2), (pic.width - 3), (pic.width - 4), (pic.width - 5)]
    avoidY = [0, 1, 2, 3, 4, 5, (pic.height - 1), (pic.height - 2), (pic.height - 3), (pic.height - 4), (pic.height - 5)]
    for i in range(0, pic.width, 1):
        for j in range(0, pic.height, 1):
            rY1,gY1,bY1 = pic.getRGB(i, j)
            rY2,gY2,bY2 = pic.getRGB(i, j+1)
            contrastY = gY1 - gY2

            rX1,gX1,bX1 = pic.getRGB(i, j)
            rX2,gX2,bX2 = pic.getRGB(i+1, j)
            contrastX = gX1 - gX2
            if contrastX != 0:
                if abs(contrastX) <= thresh1 and abs(contrastX) >= thresh2:
                    if i not in avoidX:
                        newPic.setRGB(i, j, 255, 0, 0)


            if contrastY != 0:
                if abs(contrastY) <= thresh1 and abs(contrastX) >= thresh2:
                    if j not in avoidY:
                        newPic.setRGB(i, j, 0, 255, 0)

    show(newPic, 'New')

findEdge(pic)
