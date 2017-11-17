from Myro import *
from Graphics import *

###
linePic = Picture("line.png")
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

points = findEdge()
#print(len(points))
xVal = []
yVal = []
for i in range (0,len(points),2):
    xVal.append(points[i][0])
print("XVAL:",xVal)
    
for j in range (0,len(points),2):
    yVal.append(points[j][1])
print("YVAL:",yVal)

sumX = 0
sumY = 0

for i in range (len(xVal)):
    sumX += xVal[i]
avgX = sumX / len(xVal)    
    
for j in range (len(yVal)):
    sumY += yVal[j]
avgY = sumY / len(yVal)       

print(avgX)
print(avgY)

        