from sympy import Symbol, solve
import mpmath
AA = [1,2,5]
N0 = (solve(X-AA[1])*(X-AA[2]))
D0 = (AA[0]-AA[1])*(AA[0]-AA[2])
print (N0)
