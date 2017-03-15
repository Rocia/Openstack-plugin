from __future__ import division
import random
import sympy

available = {896: 126126114111032101108267893162, 145: 126126114111032101108037789929, 66: 126126114111032101108033286850, 613: 126126114111032101108133329321, 545: 126126114111032101108112130729, 780: 126126114111032101108195947474, 602: 126126114111032101108129731474, 983: 126126114111032101108292268741, 988: 126126114111032101108294920946, 431: 126126114111032101108082173125}
recover = [ [k,v] for k, v in available.items() ]

A = []
B = []
rand = []
X = sympy.Symbol('X')
n = random.randint(0, 9)
if(n <4 ):
    print ("The system is currently incapable of recovering your data. Please try again later.")
else:
    for i in range(0,3):
        rand = random.choice(recover)
        x = rand[0]
        y = rand[1]

        A.append([x])
        B.append([y])
        recover.remove(rand)

    print(A,B)

    I0 = sympy.solve((X-A[1])(X-A[2])/((A[0]-A[1])(A[0]-A[2])))
    I1 = sympy.solve((X-A[0])(X-A[2])/((A[1]-A[0])(A[1]-A[2])))
    I2 = sympy.solve((X-A[1])(X-A[0])/((A[2]-A[1])(A[2]-A[0])))

    result = sympy.solve((B[0](I0))+(B[1](I1))+(B[2](I2)))
    print (result)






