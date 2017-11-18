from Myro import *
from Graphics import *
import math

setX = [1,2,3,4]
setY = [1,2,3,4]
devSumX = 0
devSumY = 0
sumX = 0
sumY = 0
#Calc Avg X
for i in range (len(setX)):
    sumX += setX[i]
avgX = sumX / len(setX)    

#Calc Avg Y 
for j in range (len(setY)):
    sumY += setY[j]
avgY = sumY / len(setY)       

### Stdev Equation
for i in range(len(setX)):
    devSumX += (pow(setX[i]-avgX,2))

for j in range(len(setY)):
    devSumY += (pow(setY[j]-avgY,2))


needRootX = devSumX / (len(setX) - 1)
needRootY = devSumY / (len(setY) - 1) 

devX = math.sqrt(needRootX)
devY = math.sqrt(needRootY)
###
sumAB = 0
sumAA = 0
sumBB = 0
for i in range(len(setX)):
    #A or B = point - avg x or y corresponding
    a = setX[i] - avgX
    b = setY[i] - avgY
    #Sum of A * B
    sumAB += a*b
    #Sum of A Squared
    sumAA += a*a
    #Sum of B Squared
    sumBB += b*b

r = sumAB / (math.sqrt(sumAA * sumBB))
print("R:",r)
print("stdDevX:", devX)        
print("stdDevY:", devY)
m = r*(devY / devX)
print("Slope:", m)

                