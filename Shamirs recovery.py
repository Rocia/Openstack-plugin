import random
import numpy
from numpy import matrix
from numpy import linalg
#from odict import odict


available = {912: 126126114111321011633109258,704: 126126114111321011487298666, 64: 126126114111321011086008490, 496: 126126114111321011245930570, 966: 126126114111321011700144210, 272: 126126114111321011132210698, 588: 126126114111321011311853538, 686: 126126114111321011394383650, 910: 126126114111321011630700514, 655: 126126114111321011366904289}

matrixA = []
matrixB = []
n = random.randint(0, 9)
if(n <4 ):
    print ("The system is currently incapable of recovering your data. Please try again later.")
else:
    for i in range(0,3):
        node = random.randint(0, 9)
        for key in available:
            x = key
            y = available[x]
        matrixA.append([x*x,x,1])
        matrixB.append([y])
    print (matrixA)
    print (matrixB)
    Ainv = matrixA.I
    result=Ainv * matrixB
    print(result)




