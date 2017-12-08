from Myro import *
import math
from Graphics import *
xVal = [102, 102, 102, 102, 102, 102, 102, 102, 102, 103]
yVal = [480, 482, 484, 486, 488, 490, 492, 494, 496, 476]

#xVal = [0, 10, 20, 30, 40, 50]
#yVal = [0, 20, 40, 60, 80, 100]
def regCoef():
    pic = Picture(400, 600)
    ###
    ###
    newLen = 0
    sumX = 0
    sumY = 0
    devSumX = 0
    devSumY = 0
    ###

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
    show(pic, "pic")
    global win
    win = getWindow("pic")
    r = sumAB / (math.sqrt(sumAA * sumBB))
    m = r*(devY / devX)
    lowestX = xVal.index(min(xVal))
    lowestY = yVal.index(min(yVal))
    ###
    b = yVal[0] - (m*xVal[0])
    red = makeColor(255,0,0)
    c1 = Circle((xVal[lowestX], b), 5)
    c2 = Circle((0, 0), 5)
    c1.setColor(red)
    c2.setColor(red)
    c1.draw(win)
    c2.draw(win)
    drawMyLine(m,b)
    
    print("R:",r)
    print("stdDevX:", devX)        
    print("stdDevY:", devY)
    print("Slope:", m)
    print("int:",b)  
    return [m, b]

                
def pointCalc(x,m,b):
    return (m*x)+b
  
  
def drawMyLine(m,b):
    for i in range (10):
      yhat = pointCalc(i,m,b)
      blue = makeColor(0, 0, 255)
      c = Circle((i, yhat), 5)
      c.setColor(blue)
      c.draw(win)
      
regCoef()