'''
import numpy as np
A = np.random.rand(1000, 1000, 3, 3)
identity = np.identity(3, dtype=A.dtype)
Ainv = np.zeros_like(A)
Atrans = np.zeros_like(A)
for i in range(1000):
    for j in range(1000):
        Ainv[i, j] = np.linalg.solve(A[i, j], identity)
        Atrans[i, j] = np.transpose(A[i, j])
print(Ainv)
print(Atrans)
'''

import random
import numpy as np
from numpy.linalg import inv
#from odict import odict
'''
def adjoint(A):
    """compute inverse without division by det; ...xv3xc3 input, or array of matrices assumed"""
    AI = np.empty_like(A)
    for i in range(3):
        AI[...,i,:] = np.cross(A[...,i-2,:], A[...,i-1,:])
    return AI

def inverse_transpose(A):
    """
    efficiently compute the inverse-transpose for stack of 3x3 matrices
    """
    I = adjoint(A)
    det = dot(I, A).mean(axis=-1)
    return I / det[...,None,None]

def inverse(A):
    """inverse of a stack of 3x3 matrices"""
    return np.swapaxes( inverse_transpose(A), -1,-2)
def dot(A, B):
    """dot arrays of vecs; contract over last indices"""
    return np.einsum('...i,...i->...', A, B)
'''

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

    A = np.array(matrixA)
    B = np.array(matrixB)

    print(A)
    print(B)
    Ai = np.linalg.inv(A)

    print(Ai)




