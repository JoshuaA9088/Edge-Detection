from Myro import *
from Graphics import *
import Math

grayBlock = Picture("blockG2.png")
blurImage = Picture(grayBlock)
linePic = Picture(grayBlock)
newPic = Picture(grayBlock)

jThresh = 10
iThresh = 10
jThreshHigh = 420
iThreshHigh = 250
thres1 = 25
thres2 = 1000


def findEdge():
    edge = []
    for i in range(0, linePic.width, 1):
        for j in range(0, linePic.height, 1):
            rY1, gY1, bY1 = linePic.getRGB(i, j)
            rY2, gY2, bY2 = linePic.getRGB(i, j + 1)
            contrastY = gY1 - gY2

            rX1, gX1, bX1 = linePic.getRGB(i, j)
            rX2, gX2, bX2 = linePic.getRGB(i + 1, j)
            contrastX = gX1 - gX2

            if contrastY != 0:
                if abs(contrastY) >= thres1 and abs(contrastY) <= thres2:
                    if contrastY < 0:
                        if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                            edge.append([i, j])
                            newPic.setRGB(i, j + 1, 0, 255, 0)
                        else:
                            if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                                newPic.setRGB(i, j, 0, 255, 0)
                                edge.append([i, j])

            if contrastX != 0:
                if abs(contrastX) >= thres1 and abs(contrastX) <= thres2:
                    if contrastX < 0:
                        if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                            newPic.setRGB(i, j, 0, 255, 0)
                            edge.append([i, j])
                    else:
                        newPic.setRGB(i, j, 255, 255, 255)
                else:
                    if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                        newPic.setRGB(i, j, 0, 255, 0)
                        edge.append([i, j])

    show(newPic, "New Edged")
    blur(newPic)

    return edge


def blur(pic):
    for x in range(pic.width):
        for y in range(pic.height):

            a = (x - 1, y - 1)
            b = (x - 1, y)
            c = (x - 1, y + 1)
            d = (x, y - 1)
            e = (x, y)
            f = (x, y + 1)
            g = (x + 1, y - 1)
            h = (x + 1, y)
            i = (x + 1, y + 1)

            aVal = pic.getRGB(a[0], a[1])
            bVal = pic.getRGB(b[0], b[1])
            cVal = pic.getRGB(c[0], c[1])
            dVal = pic.getRGB(d[0], d[1])
            eVal = pic.getRGB(e[0], e[1])
            fVal = pic.getRGB(f[0], f[1])
            gVal = pic.getRGB(g[0], g[1])
            hVal = pic.getRGB(h[0], h[1])
            iVal = pic.getRGB(i[0], i[1])

            avgValR = (aVal[0] + bVal[0] + cVal[0] + eVal[0] +
                       fVal[0] + gVal[0] + hVal[0] + iVal[0]) / 2
            avgValG = (aVal[1] + bVal[1] + cVal[1] + eVal[1] +
                       fVal[1] + gVal[1] + hVal[1] + iVal[1]) / 2
            avgValB = (aVal[2] + bVal[2] + cVal[2] + eVal[2] +
                       fVal[2] + gVal[2] + hVal[2] + iVal[2]) / 2

            if e[0] != -1 and e[0] != 1:
                blurImage.setRGB(e[0], e[1], avgValR, avgValG, avgValB)

            if e[1] == -1 and e[0] == 0:
                # blurImage.setRGB(e[0], e[1], 255, 0, 0)
                blurImage.setRGB(e[0], e[1], avgValR, avgValG, avgValB)

            # blurImage.setRGB(200,200,255,0,0)
    show(blurImage, "BLUR IMAGE:")
    show(pic, "ORIGINAL")


foo = findEdge()
