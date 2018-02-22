from Myro import *
from Graphics import *
import math
import csv

iThresh = 10
jThresh = 10
iThreshHigh = 426
jThreshHigh = 266
iBlack = 0
jBlack = 0 
###
linePic =Picture("blockG.png")
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
    for i in range (img.width):
        for j in range (img.height):
            r,g,b = linePic.getRGB(i, j)
            total = (r + g + b) / 3
            #print(total)
            grayImg.setRGB(i, j, total, total, total)  
    show(grayImg)

def findEdge():
    edge = []
    for i in range(0, linePic.width, 1):
        for j in range(0, linePic.height, 1):
            rY1,gY1,bY1 = linePic.getRGB(i, j)
            rY2,gY2,bY2 = linePic.getRGB(i, j+1)
            contrastY = gY1 - gY2
            #print(contrastX)
            rX1,gX1,bX1 = linePic.getRGB(i, j)
            rX2,gX2,bX2 = linePic.getRGB(i+1, j)
            contrastX = gX1 - gX2
            
            
            if contrastY != 0:
                if abs(contrastY) >= thres1 and abs(contrastY) <= thres2:
                   if contrastY < 0:
                       if i > iThresh and j > iThresh and i < iThreshHigh and j < jThreshHigh:
                        edge.append([i, j]) 
                        newPic.setRGB(i, j+1, 0,255,0)
                        #Centroid
                        global iBlack, jBlack
                        iBlack += i
                        jBlack += j
                   else:
                        if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                            newPic.setRGB(i, j, 0,255,0)
                            edge.append([i, j])
                            iBlack += i
                            jBlack += j
 
            if contrastX != 0:    
                if abs(contrastX) >= thres1 and abs(contrastX) <= thres2:
                   if contrastX < 0:
                       if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                        newPic.setRGB(i, j, 0,255,0) 
                        edge.append([i, j])
                        iBlack += i
                        jBlack += j 
                       
                   else:
                       if i > iThresh and j > jThresh and i < iThreshHigh and j < jThreshHigh:
                        newPic.setRGB(i, j, 0,255,0)
                        edge.append([i, j])
                        iBlack += i
                        jBlack += j 
                       
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
    for i in range (len(points)):
        xVal.append(points[i][0])
        newLen += 1 
#print("XVAL:",len(xVal))
    
    #Calc Y Vals ^
    for j in range (len(points)):
        yVal.append(points[j][1])
    #print("YVAL:",len(yVal))

    #Calc Avg X
    for i in range (len(xVal)):
        sumX += xVal[i]
    avgX = sumX / len(xVal)    

    #Calc Avg Y 
    for j in range (len(yVal)):
        sumY += yVal[j]
    avgY = sumY / len(yVal)       

    ### Stdev Equation
    for i in range(len(xVal)):
        devSumX += (pow(xVal[i]-avgX,2))

    for j in range(len(yVal)):
        devSumY += (pow(yVal[j]-avgY,2))

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
        #Sum of A values
        sumA = sum(xVal)
        #Sum of B Values
        sumB = sum(yVal)
        #Sum of A * B
        sumAB += (a*b)
        #Sum of A Squared
        sumAA += (a*a)
        #Sum of B Squared
        sumBB += (b*b)
        m1 += ((xVal[i] - avgX) * (yVal[i] - avgY))
        m2 += ((xVal[i] - avgX) * (xVal[i] - avgX))
        
    #m = (len(xVal) * sumAB) - (sumA * sumB) / ((len(xVal) * sumAA) - (sumAA))
    #b = ((sumB * sumAA) - (sumA * sumAB)) / ((len(xVal) * sumAA) - (sumAA))
    m = m1 / m2 
    b = avgY - (m * avgX)       
    #R value, correlation
    red = makeColor(255,0,0)

    drawMyLine(m,b)
    
    #Centroid
    iCentroid = iBlack / len(points)
    jCentroid = jBlack / len(points)
    
    #print("R:",r)
    print("stdDevX:", devX)        
    print("stdDevY:", devY)
    print("Slope:", m)
    print("int:", b)
    print("Image Height:", linePic.height)
    print("Image Width:", linePic.width)
    print("iCentroid:", iCentroid)
    print("jCentroid:", jCentroid)
    c = Circle((iCentroid, jCentroid), 10)
    c.setColor(red)
    c.draw(win)
    
    with open('x.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(xVal)
    with open('y.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(yVal)    
    return [m, b]

                
def pointCalc(x,m,b):
    y = (m*x)+b
    return y
  
def drawMyLine(m,b):
    for i in range (linePic.width):
      yhat = pointCalc(i,m,b)
      global blue, red
      blue = makeColor(0, 0, 255)
      red =  makeColor(255, 0, 0)
      c = Circle((i, yhat), 2)
      c.setColor(blue)
      c.draw(win)


regCoef()
 