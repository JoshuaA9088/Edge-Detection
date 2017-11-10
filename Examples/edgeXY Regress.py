from Myro import *
from Graphics import *

###
linePic = Picture("lineReg1.jpg")
newPic = Picture(linePic)
show(linePic, "Original")
show(newPic, "New")
win = getWindow("New")
###

###
thres1 = 80
thres2 = 0
###

def findEdge():
    edge = []
    for i in range (linePic.width):
        for j in range (linePic.height):
            rY1,gY1,bY1 = linePic.getRGB(i, j)
            rY2,gY2,bY2 = linePic.getRGB(i, j+1)
            contrastY = gY1 - gY2
            
            rX1,gX1,bX1 = linePic.getRGB(i, j)
            rX2,gX2,bX2 = linePic.getRGB(i+1, j)
            contrastX = gX1 - gX2
            
            if contrastY != 0:
                if abs(contrastY) >= thres1 or abs(contrastY) <= thres2:
                    if contrastY < 0: 
                       #newPic.setRGB(i, j+1, 255,0,255)
                       edge.append([i, j]) 
                    else:
                       #newPic.setRGB(i, j, 255,255,0)
                       edge.append([i, j]) 
            if contrastX != 0:    
                if abs(contrastX) >= thres1 or abs(contrastX) <= thres2:
                    if contrastX < 0: 
                       #newPic.setRGB(i+1, j, 255,0,255)
                       edge.append([i, j]) 
                    else:
                       #newPic.setRGB(i, j, 255,255,0)
                       edge.append([i, j]) 
    return edge       



def regCoef():
    lenEdge = len(edge)
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXX = 0
    for pt in edge:
        sumX += pt[0]
        sumY += pt[1] 
        sumXY += pt[0]*pt[1]
        sumXX += pt[0]*pt[0]
    #slope a
    slope = ((lenEdge*sumXY) - (sumX) * (sumY)) / ((lenEdge*sumXX) - sumXX)
    #int b
    intercept = (sumY - (slope*sumX)) / lenEdge
    print("Slope:",slope)
    print("Intercept:", intercept) 
    return [sumX, sumY, sumXY, sumXX, slope, intercept]
    

def myLine(x):
    m = 1
    b = 0
    return (m*x)+b

edge = findEdge()
sumR = 0
#print(edge)
weirdPoints = 0
for pt in edge:
    yhat = myLine(pt[0])
    r = yhat - pt[1]
    if abs(r) > 350:
    #print(pt[0], pt[1])
        weirdPoints += 1
    else:
        sumR += pow(r,2)
    #print(r, pt[0], pt[1], yhat)
newR = sumR/(len(edge))
print("# of weird points:", weirdPoints)
print("newR:",newR)
regCoef()

                          
def drawMyLine():
    for i in range (linePic.width):
      yhat = myLine(i)
      c = Circle((i, yhat), 2)
      c.draw(win)  