import random
import numpy as np
from numpy import matrix
from numpy.linalg import inv
#from odict import odict


available = {896: 126126114111032101108267893162, 145: 126126114111032101108037789929, 66: 126126114111032101108033286850, 613: 126126114111032101108133329321, 545: 126126114111032101108112130729, 780: 126126114111032101108195947474, 602: 126126114111032101108129731474, 983: 126126114111032101108292268741, 988: 126126114111032101108294920946, 431: 126126114111032101108082173125}

matrixA = []
matrixB = []
n = random.randint(0, 9)
if(n <4 ):
    print ("The system is currently incapable of recovering your data. Please try again later.")
else:
    for i in range(0,3):
        x = random.choice(list(available.keys()))
        y = available[x]

        matrixA.append([x*x,x,1])
        matrixB.append([y])

    A = np.array(matrixA)
    B = np.array(matrixB)

    print(A)
    print(B)
    Ai = np.linalg.inv(A)

    print(Ai)

    '''# result is 3x4
    result = [[0],
              [0],
              [0]]

    # iterate through rows of X
    for i in range(len(A)):
        # iterate through columns of Y
        for j in range(len(B[0])):
            # iterate through rows of Y
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for r in result:
        print(r)

    '''
    result = Ai * B

    print(result)

