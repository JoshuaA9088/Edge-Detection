from Myro import *
from Graphics import *
from collections import Counter
import math
import csv

jThresh = 10
iThresh = 10
jThreshHigh = 420
iThreshHigh = 250
###
linePic = Picture("blockG2.png")
newPic = Picture(linePic)
show(linePic, "Original")
show(newPic, "New")
win = getWindow("New")
grayImg = Picture(linePic)
###

###
thres1 = 25
thres2 = 1000
###


def grayscale(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = linePic.getRGB(i, j)
            total = (r + g + b) / 3
            # print(total)
            grayImg.setRGB(i, j, total, total, total)
    show(grayImg)


def findEdge():
    edge = []
    for i in range(0, linePic.width, 1):
        for j in range(0, linePic.height, 1):
            rY1, gY1, bY1 = linePic.getRGB(i, j)
            rY2, gY2, bY2 = linePic.getRGB(i, j + 1)
            contrastY = gY1 - gY2
            # print(contrastX)
            rX1, gX1, bX1 = linePic.getRGB(i, j)
            rX2, gX2, bX2 = linePic.getRGB(i + 1, j)
            contrastX = gX1 - gX2

            if contrastY != 0:
                if abs(contrastY) >= thres1 and abs(contrastY) <= thres2:
                    if contrastY < 0:
                        if i < iThresh or j < jThresh or i > iThreshHigh or j > jThreshHigh:
                            if i > iThresh - i or j > jThresh - j:
                                pass
                            pass
                        else:
                            edge.append([i, j])
                            newPic.setRGB(i, j + 1, 0, 255, 0)

                    else:
                        if i < iThresh or j < jThresh or i > iThreshHigh or j > jThreshHigh:
                            pass
                        else:
                            newPic.setRGB(i, j, 0, 255, 0)
                            edge.append([i, j])

            if contrastX != 0:
                if abs(contrastX) >= thres1 and abs(contrastX) <= thres2:
                    if contrastX < 0:
                        if i < iThresh or j < jThresh or i > iThreshHigh or j > jThreshHigh:
                            pass
                        else:
                            newPic.setRGB(i, j, 0, 255, 0)
                            edge.append([i, j])

                    else:
                        if i < iThresh or j < jThresh or i > iThreshHigh or j > jThreshHigh:
                            pass
                        else:
                            newPic.setRGB(i, j, 0, 255, 0)
                            edge.append([i, j])

    return edge


def regCoef():
    ###
    xVal = []
    yVal = []
    ###
    newLen = 0
    sumX = 0
    sumY = 0
    devSumX = 0
    devSumY = 0
    ###
    points = findEdge()
    """
    #Calc X Vals Grabs every other point to map only one edge of a line
        for i in range (0,len(points),2):
        xVal.append(points[i][0])
        newLen += 1
    #print("XVAL:",len(xVal))

    #Calc Y Vals ^
    for j in range (0,len(points),2):
        yVal.append(points[j][1])
    #print("YVAL:",len(yVal))
    """
    for i in range(len(points)):
        xVal.append(points[i][0])
        newLen += 1
# print("XVAL:",len(xVal))

    # Calc Y Vals ^
    for j in range(len(points)):
        yVal.append(points[j][1])
    # print("YVAL:",len(yVal))

    # Calc Avg X
    for i in range(len(xVal)):
        sumX += xVal[i]
    avgX = sumX / len(xVal)

    # Calc Avg Y
    for j in range(len(yVal)):
        sumY += yVal[j]
    avgY = sumY / len(yVal)

    # Stdev Equation
    for i in range(len(xVal)):
        devSumX += (pow(xVal[i] - avgX, 2))

    for j in range(len(yVal)):
        devSumY += (pow(yVal[j] - avgY, 2))

    needRootX = devSumX / (len(xVal) - 1)
    needRootY = devSumY / (len(yVal) - 1)

    devX = math.sqrt(needRootX)
    devY = math.sqrt(needRootY)
    ###
    sumAB = 0
    sumAA = 0
    sumBB = 0
    sumA = 0
    sumB = 0
    ### Correlation Calculation ###
    """
    for i in range(len(xVal)):
        #A or B = point - avg x or y corresponding
        a = xVal[i] - avgX
        b = yVal[i] - avgY
        #Sum of A * B
        sumAB += a*b
        #Sum of A Squared
        sumAA += a*a
        #Sum of B Squared
        sumBB += b*b

    r = sumAB / (math.sqrt(sumAA * sumBB))
    m = r*(devY / devX)
    b = yVal[0] - (m*xVal[0])


    """
    m1 = 0
    m2 = 0
    for i in range(len(xVal)):
        a = xVal[i]
        b = yVal[i]
        # Sum of A values
        sumA = sum(xVal)
        # Sum of B Values
        sumB = sum(yVal)
        # Sum of A * B
        sumAB += (a * b)
        # Sum of A Squared
        sumAA += (a * a)
        # Sum of B Squared
        sumBB += (b * b)
        m1 += ((xVal[i] - avgX) * (yVal[i] - avgY))
        m2 += ((xVal[i] - avgX) * (xVal[i] - avgX))

    # m = (len(xVal) * sumAB) - (sumA * sumB) / ((len(xVal) * sumAA) - (sumAA))
    # b = ((sumB * sumAA) - (sumA * sumAB)) / ((len(xVal) * sumAA) - (sumAA))
    m = m1 / m2
    b = avgY - (m * avgX)
    # R value, correlation
    global red, blue
    red = makeColor(255, 0, 0)
    blue = makeColor(0, 0, 255)

    newX = list(filter(lambda a: a != 426, xVal))
    newY = list(filter(lambda a: a != 265, yVal))
    xCounter = Counter(newX)
    yCounter = Counter(newY)

    xItem, xNumber = xCounter.most_common(1)[0]
    yItem, yNumber = yCounter.most_common(1)[0]

    print(xItem, xNumber)
    print(yItem, yNumber)

    line = Line((xItem, 0), (xItem, 266))
    line.setColor(red)
    line.border = 3
    line.draw(win)

    drawMyLine(m, b)

    """
    from Graphics import *
    win = Window("Shapes", 200, 200)
    shape = Line((10, 10), (190, 190))
    shape.fill = Color("blue")
    shape.border = 3
    shape.draw(win)
    """

    # print("R:",r)
    print("stdDevX:", devX)
    print("stdDevY:", devY)
    print("Slope:", m)
    print("int:", b)
    print("Height:", linePic.height)
    print("Width:", linePic.width)
    with open('x.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(xVal)
    with open('y.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(yVal)
    return [m, b]


def pointCalc(x, m, b):
    y = (m * x) + b
    return y


def drawMyLine(m, b):
    for i in range(linePic.width):
        yhat = pointCalc(i, m, b)
        c = Circle((i, yhat), 2)
        c.setColor(blue)
        c.draw(win)


regCoef()
