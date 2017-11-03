from Myro import *
from Graphics import *
linePic = Picture("img.jpg")
show(linePic)
newPic = Picture(linePic)
show(linePic, "Original")
show(newPic, "New")

for i in range (linePic.width):
    for j in range (linePic.height):
        rY1,gY1,bY1 = linePic.getRGB(i, j)
        rY2,gY2,bY2 = linePic.getRGB(i, j+1)
        
        contrastY = gY1 - gY2
        
        if contrastY != 0:
            #print(contrastY)
            if abs(contrastY) >= 252:
                if contrastY < 0:
                #print(contrastX)
                #print("foo")  
                    newPic.setRGB(i, j+1, 255,0,255)
                else:
                   newPic.setRGB(i, j, 255,255,0)
