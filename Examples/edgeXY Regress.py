from Myro import *
from Graphics import *
import math

###
linePic =Picture("block1.png")
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
                       edge.append([i, j]) 
                       newPic.setRGB(i, j+1, 0,255,0)
                   else:
                        newPic.setRGB(i, j, 0,255,0)
                        edge.append([i, j]) 
            if contrastX != 0:    
                if abs(contrastX) >= thres1 and abs(contrastX) <= thres2:
                   if contrastX < 0:
                       newPic.setRGB(i, j, 0,255,0) 
                       edge.append([i, j]) 
                   else:
                       newPic.setRGB(i, j, 0,255,0)
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

    #Calc X Vals Grabs every other point to map only one edge of a line
    for i in range (0,len(points),2):
        xVal.append(points[i][0])
        newLen += 1 
    #print("XVAL:",len(xVal))

    #Calc Y Vals ^
    for j in range (0,len(points),2):
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
    ### Correlation Calculation ###
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
    #R value, correlation
    r = sumAB / (math.sqrt(sumAA * sumBB))
    m = r*(devY / devX)
    lowestX = xVal.index(min(xVal))
    lowestY = yVal.index(min(yVal))
    b = yVal[lowestX]
    drawMyLine(m,b)
    
    print("R:",r)
    print("stdDevX:", devX)        
    print("stdDevY:", devY)
    print("Slope:", m)
    print("int:", b)

    return [m, b]

                
def pointCalc(x,m,b):
    return (m*x)+b
  
def drawMyLine(m,b):
    print('wrong')
    for i in range (linePic.width):
      yhat = pointCalc(i,m,b)
      blue = makeColor(0, 0, 255)
      c = Circle((i, yhat), 15)
      c.setColor(blue)
      c.draw(win)
      
regCoef()  